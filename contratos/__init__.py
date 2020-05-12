from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class Contrato:
    fornecedor: int
    mes_inicio: int
    mes_fim: int
    valor: float

    def __repr__(self):
        return f'Contrato(fornecedor={self.fornecedor + 1}, mês inicial={self.mes_inicio + 1}, mês final={self.mes_fim + 1}, valor={self.valor:.2f})'


class Contratos:
    def __init__(self, array: List[List[List[float]]], taxa: float):
        self._taxa = taxa
        self._contratos = array

    @property
    def taxa_mudanca(self) -> float:
        return self._taxa

    @property
    def num_fornecedores(self) -> int:
        return len(self._contratos)

    @property
    def num_meses(self) -> int:
        return len(self._contratos[0])

    def get_contrato(self, fornecedor: int, mes_inicial: int, mes_final: int) -> Contrato:
        return Contrato(fornecedor, mes_inicial, mes_final,
                        self._contratos[fornecedor][mes_inicial][mes_final])

    def get_contratos_periodo(self, mes_inicial: int, mes_final: int) -> List[Contrato]:
        contratos = []
        for fornecedor in range(self.num_fornecedores):
            contratos.append(self.get_contrato(
                fornecedor, mes_inicial, mes_final))
        return contratos
