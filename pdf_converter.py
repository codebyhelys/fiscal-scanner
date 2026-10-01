import fitz
from PIL import Image

def pdf_to_Images(caminho_pdf: str, dpi: int = 200)-> list[Image.Image]:
    
    imagens = []
    documento = fitz.open(caminho_pdf)
    try:
        zoom = dpi / 72
        matriz = fitz.Matrix(zoom, zoom)
        for pagina in documento:
            pixmap = pagina.get_pixmap(matrix=matriz)
            imagem = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            imagens.append(imagem)
    finally:
        documento.close()
    return imagens
          