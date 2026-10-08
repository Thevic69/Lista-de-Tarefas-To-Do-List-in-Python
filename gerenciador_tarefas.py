"""
Gerenciador de Tarefas
------------------------
Centraliza toda a lógica de manipulação das tarefas: adicionar, listar,
concluir, remover e, principalmente, salvar e carregar os dados de um
arquivo JSON, garantindo que as tarefas continuem disponíveis mesmo
depois que o programa for fechado.
"""

import json
import os

from modelo_tarefa import Tarefa


class GerenciadorDeTarefas:

    def __init__(self, caminho_do_arquivo="tarefas.json"):
        self.caminho_do_arquivo = caminho_do_arquivo
        self.tarefas = []
        self.carregar_tarefas()

    def carregar_tarefas(self):
        """Lê o arquivo JSON do disco e reconstrói a lista de tarefas em memória."""
        if not os.path.exists(self.caminho_do_arquivo):
            self.tarefas = []
            return

        try:
            with open(self.caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
                dados_salvos = json.load(arquivo)
            self.tarefas = [Tarefa.a_partir_de_dicionario(dados) for dados in dados_salvos]
        except (json.JSONDecodeError, OSError):
            # Arquivo corrompido, vazio ou inacessível: inicia com uma lista vazia
            # em vez de interromper o programa com um erro.
            self.tarefas = []

    def salvar_tarefas(self):
        """Grava o estado atual das tarefas no arquivo JSON."""
        dados_para_salvar = [tarefa.para_dicionario() for tarefa in self.tarefas]
        with open(self.caminho_do_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados_para_salvar, arquivo, indent=4, ensure_ascii=False)

    def gerar_proximo_identificador(self):
        """Calcula o próximo identificador disponível, com base no maior já existente."""
        if not self.tarefas:
            return 1
        return max(tarefa.identificador for tarefa in self.tarefas) + 1

    def adicionar_tarefa(self, descricao, prioridade="Média", prazo=None):
        nova_tarefa = Tarefa(
            identificador=self.gerar_proximo_identificador(),
            descricao=descricao,
            prioridade=prioridade,
            prazo=prazo,
        )
        self.tarefas.append(nova_tarefa)
        self.salvar_tarefas()
        return nova_tarefa

    def listar_tarefas(self, apenas_pendentes=False):
        """Retorna as tarefas cadastradas, ordenadas por identificador."""
        tarefas_ordenadas = sorted(self.tarefas, key=lambda tarefa: tarefa.identificador)

        if apenas_pendentes:
            return [tarefa for tarefa in tarefas_ordenadas if not tarefa.concluida]

        return tarefas_ordenadas

    def buscar_tarefa_por_identificador(self, identificador):
        for tarefa in self.tarefas:
            if tarefa.identificador == identificador:
                return tarefa
        return None

    def concluir_tarefa(self, identificador):
        tarefa_encontrada = self.buscar_tarefa_por_identificador(identificador)

        if tarefa_encontrada is None:
            return False

        tarefa_encontrada.marcar_como_concluida()
        self.salvar_tarefas()
        return True

    def remover_tarefa(self, identificador):
        tarefa_encontrada = self.buscar_tarefa_por_identificador(identificador)

        if tarefa_encontrada is None:
            return False

        self.tarefas.remove(tarefa_encontrada)
        self.salvar_tarefas()
        return True
