from decimal import Decimal
from pydantic import BaseModel, Field

class Item(BaseModel):
    descricao : str
    quantidade : float
    valor_unitario : Decimal
    valor_total : Decimal

class NotaFiscal(BaseModel):
    empresa : str = Field(description="Razão social ou nome fantasia do emitente")
    cnpj : str = Field(decription="CNPJ como aparece na nota, com ou sem máscara")
    data_emissao : str = Field(description="Data de emissao no formato DD/MM/AAAA")
    valor_total : Decimal
    itens : list[Item]