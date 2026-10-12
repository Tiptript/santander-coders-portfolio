"""
Sistema de Gerenciamento de Usuários (CRUD em Python com Persistência em JSON)
Projeto desenvolvido durante o programa Santander Coders.

Conceitos aplicados:
- Persistência de Dados em Arquivo JSON (leitura, escrita e serialização)
- Operações de CRUD (Create, Read, Update, Delete)
- Padrão Soft Delete (exclusão lógica com flag 'Status')
- Manipulação de Dicionários Dinâmicos e Parâmetros com *args
- Tratamento de Exceções e Interface de Linha de Comando (CLI)
"""

import json
import os
from typing import Dict, Any

ARQUIVO_PADRAO = os.path.join(os.path.dirname(__file__), "usuarios_database.json")


def ler_arquivo_usuarios(nome_arquivo: str = ARQUIVO_PADRAO) -> Dict[str, Dict[str, Any]]:
    """Carrega o dicionário de usuários a partir do arquivo JSON."""
    if not os.path.exists(nome_arquivo):
        return {}
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print(f"[AVISO] Não foi possível ler '{nome_arquivo}'. Iniciando banco vazio.")
        return {}


def salvar_arquivo_usuarios(usuarios: Dict[str, Dict[str, Any]], nome_arquivo: str = ARQUIVO_PADRAO):
    """Salva o dicionário de usuários em disco formatado com indentação legível."""
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        print("💾 Alterações salvas com sucesso em disco!")
    except IOError as e:
        print(f"[ERRO] Falha ao gravar arquivo JSON: {e}")


def inserir_usuario(
    usuarios: Dict[str, Dict[str, Any]], nome: str, telefone: str = "vazio", endereco: str = "vazio"
) -> str:
    """Insere um novo usuário com ID incremental ou reativa caso já exista idêntico."""
    nome = nome.strip()
    telefone = telefone.strip()
    endereco = endereco.strip()

    # Verifica se já existe um usuário com mesmos dados cadastrais
    for user_id, dados in usuarios.items():
        if dados.get("Nome") == nome and dados.get("Telefone") == telefone and dados.get("Endereço") == endereco:
            if not dados.get("Status", True):
                dados["Status"] = True
                print(f"🔄 Usuário já cadastrado anteriormente. O ID {user_id} foi reativado!")
            else:
                print(f"⚠️  Usuário idêntico já existe ativo com o ID {user_id}.")
            return user_id

    # Gera próximo ID numérico sequencial
    ids_existentes = [int(k) for k in usuarios.keys() if k.isdigit()]
    proximo_id = str(max(ids_existentes, default=0) + 1)

    usuarios[proximo_id] = {
        "Status": True,
        "Nome": nome,
        "Telefone": telefone,
        "Endereço": endereco,
    }
    print(f"✅ Usuário cadastrado com sucesso! [ID: {proximo_id}]")
    return proximo_id


def excluir_usuario(usuarios: Dict[str, Dict[str, Any]], *ids: str):
    """Realiza exclusão lógica (soft delete) marcando Status como False."""
    for raw_id in ids:
        user_id = str(raw_id).strip()
        if user_id in usuarios:
            if not usuarios[user_id].get("Status", True):
                print(f"ℹ️  O usuário com ID {user_id} já se encontra inativo.")
            else:
                usuarios[user_id]["Status"] = False
                print(f"🗑️  Usuário com ID {user_id} ({usuarios[user_id].get('Nome')}) desativado com sucesso.")
        else:
            print(f"❌ Usuário com ID {user_id} não encontrado.")


def atualizar_usuario(usuarios: Dict[str, Dict[str, Any]], user_id: str):
    """Atualiza seletivamente os campos de um usuário existente."""
    user_id = str(user_id).strip()
    if user_id not in usuarios:
        print(f"❌ Usuário com ID {user_id} não foi encontrado!")
        return

    usuario = usuarios[user_id]
    print(f"\n--- Editando Usuário [ID: {user_id}] ---")
    while True:
        print(f"1 - Nome:     {usuario.get('Nome')}")
        print(f"2 - Telefone: {usuario.get('Telefone')}")
        print(f"3 - Endereço: {usuario.get('Endereço')}")
        print("0 - Concluir alterações")

        opcao = input("Qual campo deseja alterar? (0-3): ").strip()
        if opcao == "1":
            novo_nome = input("Novo nome: ").strip()
            if novo_nome:
                usuario["Nome"] = novo_nome
        elif opcao == "2":
            novo_tel = input("Novo telefone: ").strip()
            if novo_tel:
                usuario["Telefone"] = novo_tel
        elif opcao == "3":
            novo_end = input("Novo endereço: ").strip()
            if novo_end:
                usuario["Endereço"] = novo_end
        elif opcao == "0":
            print(f"✅ Atualização do ID {user_id} concluída.")
            break
        else:
            print("[AVISO] Opção inválida.")


def exibir_um_usuario(usuarios: Dict[str, Dict[str, Any]], user_id: str):
    """Exibe todos os dados detalhados de um usuário específico."""
    user_id = str(user_id).strip()
    if user_id in usuarios:
        u = usuarios[user_id]
        status_label = "Ativo" if u.get("Status", True) else "Inativo (Excluído)"
        print("\n" + "-" * 35)
        print(f"  Informações do Usuário ID: {user_id}")
        print("-" * 35)
        print(f"Nome:     {u.get('Nome')}")
        print(f"Telefone: {u.get('Telefone')}")
        print(f"Endereço: {u.get('Endereço')}")
        print(f"Status:   {status_label}")
        print("-" * 35)
    else:
        print(f"❌ Usuário com ID {user_id} não encontrado!")


def exibir_todos_usuarios(usuarios: Dict[str, Dict[str, Any]], exibir_inativos: bool = False):
    """Lista usuários cadastrados no banco de dados."""
    selecionados = {
        uid: dados
        for uid, dados in usuarios.items()
        if exibir_inativos or dados.get("Status", True)
    }

    if not selecionados:
        print("\nNenhum usuário ativo para exibir.")
        return

    print("\n" + "=" * 55)
    print(f"  LISTA DE USUÁRIOS ({len(selecionados)} cadastros)")
    print("=" * 55)
    for uid, dados in sorted(selecionados.items(), key=lambda x: int(x[0]) if x[0].isdigit() else x[0]):
        status_tag = "" if dados.get("Status", True) else " [INATIVO]"
        print(
            f"ID {uid:3} | {dados.get('Nome', ''):<18} | "
            f"Tel: {dados.get('Telefone', ''):<12} | "
            f"{dados.get('Endereço', '')}{status_tag}"
        )
    print("=" * 55)


def main():
    usuarios = ler_arquivo_usuarios()
    print("=" * 55)
    print("   📋 SISTEMA CRUD COM PERSISTÊNCIA EM ARQUIVO JSON")
    print("=" * 55)
    print(f"Total de registros carregados: {len(usuarios)}")

    while True:
        print("\n--- MENU DE OPERAÇÕES ---")
        print("1 - Inserir novo usuário")
        print("2 - Excluir usuário (Soft Delete)")
        print("3 - Atualizar dados de um usuário")
        print("4 - Consultar um usuário por ID")
        print("5 - Listar todos os usuários ativos")
        print("6 - Listar todos (incluindo inativos)")
        print("7 - Salvar e Sair")

        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == "1":
            nome = input("Nome do usuário: ").strip()
            telefone = input("Telefone: ").strip() or "vazio"
            endereco = input("Endereço: ").strip() or "vazio"
            if nome:
                inserir_usuario(usuarios, nome, telefone, endereco)
                salvar_arquivo_usuarios(usuarios)
            else:
                print("[ERRO] O nome não pode ser vazio.")

        elif opcao == "2":
            ids_entrada = input("Digite o(s) ID(s) para excluir (separados por vírgula): ").split(",")
            ids_limpos = [i.strip() for i in ids_entrada if i.strip()]
            if ids_limpos:
                excluir_usuario(usuarios, *ids_limpos)
                salvar_arquivo_usuarios(usuarios)
            else:
                print("[AVISO] Nenhum ID informado.")

        elif opcao == "3":
            id_atualizar = input("Digite o ID para atualizar: ").strip()
            atualizar_usuario(usuarios, id_atualizar)
            salvar_arquivo_usuarios(usuarios)

        elif opcao == "4":
            id_consultar = input("Digite o ID para consultar: ").strip()
            exibir_um_usuario(usuarios, id_consultar)

        elif opcao == "5":
            exibir_todos_usuarios(usuarios, exibir_inativos=False)

        elif opcao == "6":
            exibir_todos_usuarios(usuarios, exibir_inativos=True)

        elif opcao == "7":
            salvar_arquivo_usuarios(usuarios)
            print("\nSistema encerrado. Até breve!")
            break

        else:
            print("[AVISO] Opção inválida. Digite um número de 1 a 7.")


if __name__ == "__main__":
    main()
