import argparse
import json

from dotenv import load_dotenv

from pdf_converter import pdf_to_Images
from extrator import extrair_nota

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Processar arquivos PDF e extrair informações.")
    parser.add_argument("pdf_path", type=str, help="Caminho para o arquivo PDF da nota fiscal")
    args = parser.parse_args()

    imagens = pdf_to_Images(args.pdf_path)
    nota = extrair_nota(imagens)

    print(json.dumps(nota.model_dump(mode="json"), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()