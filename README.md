# fiscal-scanner 

Porjeto que ler nota fiscal em PDF e tirar os dados dela(empresa, CNPJ, data, items, total) automatimante usando IA, sem precisar digitar nada na mão.

comecei por um script simples em python só pra validar se a ideia funciona antes de montar a parte web (Django + Celery). A ideia é: joga o PDF, a Claude API olha a imagem e devolve os dados já estruturados e validados.

## como rodar hj
```bash
python -m venv .venv
source .venv/Scripts/activate]
pip install -r requirements.txt
cp .env.example .env
```

cola sua 'ANTHROPIC_API_KEY no `.env` e roda:

```bash
python main.py caminho/da/nota.pdf
```

Se não tiver uma nota real pra testar, tem um script que gera uma fake:

```bash
python gerar_pdf_teste.py
python main.py samples/nota_fake.pdf
```

Isso aqui ainda é só a base. Falta:

- pré-processar a imagem antes de mandar pra IA (rotação, contraste)
- validar os dados que voltam (CNPJ de verdade, data que faz sentido, soma dos itens batendo com o total)
- ler a chave de acesso de 44 dígitos da NF-e
- a parte web: Django pra upload, Celery pra processar em fila
- testar com um monte de notas de verdade e ver a precisão

Projeto de portfólio, então vou documentando conforme for avançando.