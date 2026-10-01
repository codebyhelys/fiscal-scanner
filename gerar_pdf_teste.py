import fitz

SAIDA = 'samples/nota_fake.pdf'

TEXTO = """NOTA FISCAL ELETRONICA - DANFE

Emitente: Padaria Pao Quente LTDA
CNPJ: 11.222.333/0001-81
Data de Emissao: 15/03/2026

Itens:
Pao Frances          qtd: 10   valor unit: 0.50    valor total: 5.00
Cafe em Graos        qtd: 2    valor unit: 25.00   valor total: 50.00
Leite Integral 1L    qtd: 6    valor unit: 4.50    valor total: 27.00

VALOR TOTAL DA NOTA: R$ 82.00
"""

documento = fitz.open()
pagina = documento.new.page()
pagina.insert_txt((50, 50), TEXTO, fontsize=11)
documento.save(SAIDA)
documento.close()

print(f"PDF de teste gerado em: {SAIDA}")
