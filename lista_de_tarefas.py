#!/usr/bin/env python3
"""
Lista de Tarefas (To-Do List)
-------------------------------
Programa de linha de comando para organizar tarefas do dia a dia.
Permite adicionar, listar, concluir e remover tarefas, com persistência
automática em um arquivo JSON, para que nada se perca ao fechar o programa.
"""

from datetime import datetime

from gerenciador_tarefas import GerenciadorDeTarefas
from modelo_tarefa import PRIORIDADES_VALIDAS

FORMATO_DE_DATA = "%d/%m/%Y"


def exibir_cabecalho():
    print("\n" + "=" * 40)
    print("           LISTA DE TAREFAS")
    print("=" * 40)


def exibir_menu_principal():
    print("\nO que você deseja fazer?")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


def solicitar_opcao_do_menu():
    opcao_escolhida = input("\nEscolha uma opção (1-5): ").strip()
    return opcao_escolhida


def solicitar_descricao_da_tarefa():
    while True:
        descricao = input("Descrição da tarefa: ").strip()
        if descricao:
            return descricao
        print("A descrição não pode ficar em branco. Tente novamente.")


def solicitar_prioridade_da_tarefa():
    print("\nPrioridade da tarefa:")
    for indice, prioridade in enumerate(PRIORIDADES_VALIDAS, start=1):
        print(f"{indice}. {prioridade}")

    escolha = input("Escolha a prioridade (padrão: Média): ").strip()

    if not escolha:
        return "Média"

    if escolha.isdigit() and 1 <= int(escolha) <= len(PRIORIDADES_VALIDAS):
        return PRIORIDADES_VALIDAS[int(escolha) - 1]

    print("Opção inválida. A prioridade padrão (Média) será utilizada.")
    return "Média"


def solicitar_prazo_da_tarefa():
    while True:
        prazo_digitado = input("Prazo (formato DD/MM/AAAA, opcional): ").strip()

        if not prazo_digitado:
            return None

        try:
            datetime.strptime(prazo_digitado, FORMATO_DE_DATA)
            return prazo_digitado
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA ou deixe em branco.")


def solicitar_identificador_da_tarefa():
    identificador_digitado = input("Digite o número da tarefa: ").strip()

    if not identificador_digitado.isdigit():
        return None

    return int(identificador_digitado)


def formatar_tarefa_para_exibicao(tarefa):
    marcador_de_status = "[X]" if tarefa.concluida else "[ ]"
    linha = f"{marcador_de_status} #{tarefa.identificador} - {tarefa.descricao} (Prioridade: {tarefa.prioridade})"

    if tarefa.prazo:
        linha += f" (Prazo: {tarefa.prazo})"

    return linha


def executar_adicionar_tarefa(gerenciador_de_tarefas):
    print("\n--- Adicionar Tarefa ---")
    descricao = solicitar_descricao_da_tarefa()
    prioridade = solicitar_prioridade_da_tarefa()
    prazo = solicitar_prazo_da_tarefa()

    nova_tarefa = gerenciador_de_tarefas.adicionar_tarefa(descricao, prioridade, prazo)
    print(f"\nTarefa adicionada com sucesso! (#{nova_tarefa.identificador})")


def executar_listar_tarefas(gerenciador_de_tarefas):
    print("\n--- Lista de Tarefas ---")
    tarefas = gerenciador_de_tarefas.listar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa cadastrada até o momento.")
        return

    for tarefa in tarefas:
        print(formatar_tarefa_para_exibicao(tarefa))

    total_de_tarefas = len(tarefas)
    total_de_concluidas = sum(1 for tarefa in tarefas if tarefa.concluida)
    print(f"\nTotal: {total_de_tarefas} tarefa(s) | Concluídas: {total_de_concluidas}")


def executar_concluir_tarefa(gerenciador_de_tarefas):
    print("\n--- Concluir Tarefa ---")

    if not gerenciador_de_tarefas.listar_tarefas():
        print("Não há tarefas cadastradas para concluir.")
        return

    executar_listar_tarefas(gerenciador_de_tarefas)
    identificador = solicitar_identificador_da_tarefa()

    if identificador is None:
        print("Número de tarefa inválido.")
        return

    tarefa_foi_concluida = gerenciador_de_tarefas.concluir_tarefa(identificador)

    if tarefa_foi_concluida:
        print(f"\nTarefa #{identificador} marcada como concluída!")
    else:
        print(f"\nNenhuma tarefa encontrada com o número #{identificador}.")


def executar_remover_tarefa(gerenciador_de_tarefas):
    print("\n--- Remover Tarefa ---")

    if not gerenciador_de_tarefas.listar_tarefas():
        print("Não há tarefas cadastradas para remover.")
        return

    executar_listar_tarefas(gerenciador_de_tarefas)
    identificador = solicitar_identificador_da_tarefa()

    if identificador is None:
        print("Número de tarefa inválido.")
        return

    confirmacao = input(f"Tem certeza que deseja remover a tarefa #{identificador}? (s/n): ").strip().lower()

    if confirmacao != "s":
        print("Remoção cancelada.")
        return

    tarefa_foi_removida = gerenciador_de_tarefas.remover_tarefa(identificador)

    if tarefa_foi_removida:
        print(f"\nTarefa #{identificador} removida com sucesso!")
    else:
        print(f"\nNenhuma tarefa encontrada com o número #{identificador}.")


def executar_loop_principal():
    gerenciador_de_tarefas = GerenciadorDeTarefas()
    exibir_cabecalho()

    acoes_do_menu = {
        "1": executar_adicionar_tarefa,
        "2": executar_listar_tarefas,
        "3": executar_concluir_tarefa,
        "4": executar_remover_tarefa,
    }

    while True:
        exibir_menu_principal()
        opcao_escolhida = solicitar_opcao_do_menu()

        if opcao_escolhida == "5":
            print("\nAté logo!")
            break

        acao_correspondente = acoes_do_menu.get(opcao_escolhida)

        if acao_correspondente is None:
            print("\nOpção inválida. Escolha um número entre 1 e 5.")
            continue

        acao_correspondente(gerenciador_de_tarefas)


if __name__ == "__main__":
    executar_loop_principal()
