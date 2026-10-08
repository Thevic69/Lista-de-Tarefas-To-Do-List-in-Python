"""
Modelo de Tarefa
-----------------
Define a estrutura de dados que representa uma única tarefa da lista,
além das funções de conversão entre o objeto Tarefa e o formato de
dicionário utilizado para salvar e carregar o arquivo JSON.
"""

from dataclasses import dataclass
from typing import Optional


PRIORIDADES_VALIDAS = ("Baixa", "Média", "Alta")


@dataclass
class Tarefa:
    identificador: int
    descricao: str
    prioridade: str = "Média"
    prazo: Optional[str] = None
    concluida: bool = False

    def marcar_como_concluida(self):
        self.concluida = True

    def para_dicionario(self):
        """Converte a tarefa em um dicionário, pronto para ser salvo em JSON."""
        return {
            "identificador": self.identificador,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "prazo": self.prazo,
            "concluida": self.concluida,
        }

    @staticmethod
    def a_partir_de_dicionario(dados):
        """Reconstrói uma tarefa a partir de um dicionário lido do JSON."""
        return Tarefa(
            identificador=dados["identificador"],
            descricao=dados["descricao"],
            prioridade=dados.get("prioridade", "Média"),
            prazo=dados.get("prazo"),
            concluida=dados.get("concluida", False),
        )
