import base64
from io import BytesIO

import anthropic
from PIL import Image

from schemas import NotaFiscal

MODEL = "claude-sonnen-5"
TOOL_NAME = "extrator"

def _forcar_valores_monetarios_como_string(schema: dict) -> dict:
    grupos_de_prioridades = [schema.get("properties", {})]
    gruupos_de_prioridades += [
        definicao.get("properties", {}) for definicao in schema.get("$defs", {}).values()
    ]
    for propriedades in grupos_de_prioridades:
        for prop in propriedades.values():
            opcoes = prop.pop("anyOf", None)
            if opcoes :
                prop.update(next(o for o in opcoes if o.get("type") == "string"))
    return schema

def _imagem_para_base64(imagem: Image.Image) -> str:
    buffer = BytesIO()
    imagem.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def extrair_nota(imagens: list[Image.Image]) -> NotaFiscal:
    client = anthropic.Anthropic()

    content = [{"type": "text", "text":"Extraia os dados extruturados desta nota fiscal."}]
    for imagem in imagens:
        content.append(
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": _imagem_para_base64(imagem),
                },
            }
        )

        schema = _forcar_valores_monetarios_como_string(NotaFiscal.model_json_schema())

        resposta = client.completions.create(
            model=MODEL,
            max_tokens_to_sample=2048,
            tools=[
                {
                    "name": TOOL_NAME,
                    "description": "Recebe os dados extraídos de uma nota fiscal",
                    "input_schema": schema,
                }
            ],
            tool_choice={"type": "tool", "name": TOOL_NAME},
            messages=[{"role": "user", "content": content}],
        )

        bloco = next(b for b in resposta.content if b.type == "tools_use")
        return NotaFiscal(**bloco.input)
        