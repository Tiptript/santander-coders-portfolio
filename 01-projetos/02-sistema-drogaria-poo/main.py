"""
Sistema de Gerenciamento de Drogaria (Programação Orientada a Objetos em Python)
Projeto desenvolvido durante o programa Santander Coders.

Conceitos aplicados:
- Classes e Construtores (__init__)
- Encapsulamento e Métodos de Instância
- Relações entre Objetos (Venda composta por Cliente e Medicamentos)
- Manipulação de Datas com datetime
- Regras de Negócio, Validações e Relatórios Estatísticos
"""

from datetime import datetime, date
from typing import List, Optional


class Laboratorio:
    """Representa um laboratório farmacêutico fabricante de medicamentos."""

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self) -> str:
        return f"<Laboratorio: {self.nome} ({self.cidade}/{self.estado})>"


class Medicamento:
    """Representa um produto farmacêutico com precificação e regras de retenção de receita."""

    def __init__(
        self,
        nome: str,
        principal_composto: str,
        laboratorio: str,
        descricao: str,
        preco: float,
        tipo_medicamento: str,
        necessita_receita: bool = False,
    ):
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.preco = float(preco)
        self.tipo_medicamento = tipo_medicamento.strip().lower()
        self.necessita_receita = necessita_receita

    def __repr__(self) -> str:
        return f"<Medicamento: {self.nome} - R${self.preco:.2f} [{self.tipo_medicamento}]>"


class Cliente:
    """Representa um cliente com validação de formato de data de nascimento."""

    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        self.cpf = cpf.strip()
        self.nome = nome.strip()
        self.data_nascimento = self._converter_data(data_nascimento)

    @staticmethod
    def _converter_data(data_str: str) -> Optional[date]:
        """Converte uma string 'dd/mm/aaaa' para date, tratando erros de formato."""
        try:
            return datetime.strptime(data_str.strip(), "%d/%m/%Y").date()
        except ValueError:
            print("[AVISO] Formato de data inválido. Use 'dd/mm/aaaa'. Data definida como vazia.")
            return None

    @property
    def idade(self) -> int:
        """Calcula a idade em anos completos com base na data atual."""
        if not self.data_nascimento:
            return 0
        hoje = datetime.now().date()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade

    def __repr__(self) -> str:
        return f"<Cliente: {self.nome} (CPF: {self.cpf}, {self.idade} anos)>"


class Venda:
    """Representa uma transação de venda vinculada a um cliente e múltiplos medicamentos."""

    def __init__(self, data_hora: datetime, produtos: List[Medicamento], cliente: Cliente, valor_total: float):
        self.data_hora = data_hora
        self.produtos = produtos
        self.cliente = cliente
        self.valor_total = valor_total

    def __repr__(self) -> str:
        return f"<Venda: {len(self.produtos)} itens para {self.cliente.nome} | Total: R${self.valor_total:.2f}>"


# =====================================================================
# Repositórios em memória
# =====================================================================
clientes: List[Cliente] = []
medicamentos: List[Medicamento] = []
laboratorios: List[Laboratorio] = []
vendas: List[Venda] = []


def carregar_dados_iniciais():
    """Popula a memória com registros iniciais de exemplo para facilitar testes rápidos."""
    lab_pfizer = Laboratorio("Pfizer", "Av. Nações Unidas, 1000", "11-3000-1111", "São Paulo", "SP")
    lab_herbarium = Laboratorio("Herbarium", "R. das Ervas, 45", "41-3200-2222", "Curitiba", "PR")
    laboratorios.extend([lab_pfizer, lab_herbarium])

    medicamentos.append(
        Medicamento(
            nome="Imatinibe",
            principal_composto="Mesilato de Imatinibe",
            laboratorio="Pfizer",
            descricao="Antineoplásico indicado para tratamento de leucemia.",
            preco=120.00,
            tipo_medicamento="quimioterápico",
            necessita_receita=True,
        )
    )
    medicamentos.append(
        Medicamento(
            nome="Cisplatina",
            principal_composto="Cisplatina",
            laboratorio="Pfizer",
            descricao="Agente quimioterápico para tumores sólidos.",
            preco=180.50,
            tipo_medicamento="quimioterápico",
            necessita_receita=True,
        )
    )
    medicamentos.append(
        Medicamento(
            nome="Passiflora",
            principal_composto="Extrato seco de Passiflora incarnata",
            laboratorio="Herbarium",
            descricao="Calmante natural fitoterápico.",
            preco=35.00,
            tipo_medicamento="fitoterápico",
            necessita_receita=False,
        )
    )
    medicamentos.append(
        Medicamento(
            nome="Ginkgo Biloba",
            principal_composto="Extrato de Ginkgo Biloba",
            laboratorio="Herbarium",
            descricao="Fitoterápico indicado para circulação e memória.",
            preco=48.90,
            tipo_medicamento="fitoterápico",
            necessita_receita=False,
        )
    )

    clientes.append(Cliente("111.222.333-44", "Dona Maria da Silva", "15/05/1950"))  # > 65 anos
    clientes.append(Cliente("555.666.777-88", "Carlos Drummond", "20/10/1988"))      # < 65 anos


def obter_opcao_inteira(mensagem: str) -> Optional[int]:
    """Lê um número inteiro do usuário com proteção contra entradas inválidas."""
    entrada = input(mensagem).strip()
    try:
        return int(entrada)
    except ValueError:
        print("[ERRO] Por favor, digite um número válido.")
        return None


# =====================================================================
# Operações de Cadastro
# =====================================================================
def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    cpf = input("CPF do cliente (ex: 123.456.789-00): ").strip()
    if any(c.cpf == cpf for c in clientes):
        print("[AVISO] Já existe um cliente com este CPF.")
        return

    nome = input("Nome do cliente: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    novo_cliente = Cliente(cpf, nome, data_nascimento)
    clientes.append(novo_cliente)
    print(f"✅ Cliente '{nome}' cadastrado com sucesso!")


def cadastrar_medicamento():
    print("\n--- Cadastro de Medicamento ---")
    nome = input("Nome do medicamento: ").strip()
    principal_composto = input("Principal composto ativo: ").strip()
    laboratorio = input("Nome do laboratório: ").strip()
    descricao = input("Descrição / Indicação: ").strip()

    tipo = input("Tipo do medicamento [1- Quimioterápico | 2- Fitoterápico]: ").strip().lower()
    if tipo in ["1", "quimioterapico", "quimioterápico"]:
        tipo_medicamento = "quimioterápico"
        necessita_receita = input("Necessita de retenção de receita? (S/N): ").strip().lower() == "s"
    elif tipo in ["2", "fitoterapico", "fitoterápico"]:
        tipo_medicamento = "fitoterápico"
        necessita_receita = False
    else:
        print("[ERRO] Tipo de medicamento inválido.")
        return

    try:
        preco = float(input("Preço unitário em R$ (ex: 29.90): ").replace(",", "."))
    except ValueError:
        print("[ERRO] Preço inválido.")
        return

    novo_medicamento = Medicamento(
        nome=nome,
        principal_composto=principal_composto,
        laboratorio=laboratorio,
        descricao=descricao,
        preco=preco,
        tipo_medicamento=tipo_medicamento,
        necessita_receita=necessita_receita,
    )
    medicamentos.append(novo_medicamento)
    print(f"✅ Medicamento '{nome}' cadastrado com sucesso!")


# =====================================================================
# Processamento de Venda
# =====================================================================
def realizar_venda():
    print("\n--- Realizar Nova Venda ---")
    if not clientes:
        print("[AVISO] Nenhum cliente cadastrado. Cadastre um cliente antes.")
        return
    if not medicamentos:
        print("[AVISO] Nenhum medicamento em estoque. Cadastre medicamentos antes.")
        return

    cpf_cliente = input("Digite o CPF do cliente: ").strip()
    cliente = next((c for c in clientes if c.cpf == cpf_cliente), None)

    if cliente is None:
        print(f"[ERRO] Cliente com CPF '{cpf_cliente}' não encontrado.")
        return

    print(f"Cliente selecionado: {cliente.nome} (Idade: {cliente.idade} anos)")

    carrinho: List[Medicamento] = []
    print("\nAdicione produtos ao carrinho (digite 'fim' para concluir):")
    while True:
        nome_produto = input("Nome do medicamento (ou 'fim'): ").strip()
        if nome_produto.lower() in ["fim", "sair", "0"]:
            break

        produto = next((m for m in medicamentos if m.nome.lower() == nome_produto.lower()), None)
        if produto is None:
            print(f"[AVISO] Produto '{nome_produto}' não encontrado no catálogo.")
            print("Produtos disponíveis:", ", ".join(m.nome for m in medicamentos))
            continue

        carrinho.append(produto)
        print(f"  + Adicionado: {produto.nome} (R${produto.preco:.2f})")

    if not carrinho:
        print("[AVISO] Nenhum produto adicionado. Venda cancelada.")
        return

    # Verificação de retenção de receita médica
    controlados = [p for p in carrinho if p.necessita_receita]
    if controlados:
        print("\n⚠️  [ALERTA DE RECEITA MÉDICA] Medicamentos controlados detectados:")
        for med in controlados:
            print(f"   • {med.nome} (Exige retenção de receita)")
        confirmacao = input("A receita foi conferida e validada pelo farmacêutico? (S/N): ").strip().lower()
        if confirmacao != "s":
            print("❌ Venda cancelada devido à ausência de receita médica válida.")
            return

    # Cálculo dos descontos
    subtotal = sum(p.preco for p in carrinho)
    valor_final = subtotal
    descontos_aplicados = []

    # Regra 1: Desconto de 20% para maiores de 65 anos
    if cliente.idade > 65:
        valor_final *= 0.80
        descontos_aplicados.append("20% por idade (> 65 anos)")

    # Regra 2: Desconto de 10% para compras acima de R$ 150,00
    if valor_final > 150.0:
        valor_final *= 0.90
        descontos_aplicados.append("10% por valor total (> R$ 150)")

    nova_venda = Venda(
        data_hora=datetime.now(),
        produtos=carrinho,
        cliente=cliente,
        valor_total=valor_final,
    )
    vendas.append(nova_venda)

    print("\n" + "=" * 45)
    print("         RESUMO DA VENDA")
    print("=" * 45)
    print(f"Data/Hora: {nova_venda.data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Cliente:   {cliente.nome}")
    print(f"Itens ({len(carrinho)}):")
    for item in carrinho:
        print(f"  - {item.nome:20} R${item.preco:8.2f}")
    print("-" * 45)
    print(f"Subtotal:      R${subtotal:8.2f}")
    if descontos_aplicados:
        print(f"Descontos:     {', '.join(descontos_aplicados)}")
    print(f"VALOR TOTAL:   R${valor_final:8.2f}")
    print("=" * 45)
    print("✅ Venda finalizada com sucesso!\n")


# =====================================================================
# Emissão de Relatórios e Estatísticas
# =====================================================================
def emitir_relatorios():
    while True:
        print("\n--- Módulo de Relatórios ---")
        print("1. Listagem de clientes por ordem alfabética")
        print("2. Listagem de medicamentos por ordem alfabética")
        print("3. Listagem de medicamentos quimioterápicos")
        print("4. Listagem de medicamentos fitoterápicos")
        print("5. Estatísticas dos atendimentos realizados no dia")
        print("0. Voltar ao menu principal")

        opcao = obter_opcao_inteira("Escolha uma opção: ")
        if opcao == 0:
            break
        elif opcao == 1:
            listar_clientes_ordenados()
        elif opcao == 2:
            listar_medicamentos_ordenados()
        elif opcao == 3:
            listar_medicamentos_por_tipo("quimioterápico")
        elif opcao == 4:
            listar_medicamentos_por_tipo("fitoterápico")
        elif opcao == 5:
            exibir_estatisticas_atendimentos()
        else:
            print("[AVISO] Opção inválida.")


def listar_clientes_ordenados():
    print("\n--- Clientes Cadastrados (Ordem Alfabética) ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for c in sorted(clientes, key=lambda x: x.nome):
        data_fmt = c.data_nascimento.strftime("%d/%m/%Y") if c.data_nascimento else "N/A"
        print(f"• Nome: {c.nome:<25} | CPF: {c.cpf} | Nasc: {data_fmt} ({c.idade} anos)")


def listar_medicamentos_ordenados():
    print("\n--- Catálogo de Medicamentos (Ordem Alfabética) ---")
    if not medicamentos:
        print("Nenhum medicamento cadastrado.")
        return
    for m in sorted(medicamentos, key=lambda x: x.nome):
        print(
            f"• {m.nome:<18} | Preço: R${m.preco:6.2f} | Tipo: {m.tipo_medicamento:<14} | "
            f"Composto: {m.principal_composto} ({m.laboratorio})"
        )


def listar_medicamentos_por_tipo(tipo_desejado: str):
    print(f"\n--- Medicamentos {tipo_desejado.capitalize()}s ---")
    filtrados = [m for m in medicamentos if m.tipo_medicamento == tipo_desejado]
    if not filtrados:
        print(f"Nenhum medicamento do tipo '{tipo_desejado}' cadastrado.")
        return
    for m in filtrados:
        receita_aviso = "SIM" if m.necessita_receita else "NÃO"
        print(
            f"• {m.nome:<18} | R${m.preco:6.2f} | Receita Obrigatória: {receita_aviso:<3} | "
            f"Lab: {m.laboratorio} | Composto: {m.principal_composto}"
        )


def exibir_estatisticas_atendimentos():
    print("\n--- Estatísticas do Dia ---")
    if not vendas:
        print("Nenhuma venda realizada até o momento.")
        return

    total_vendas = len(vendas)
    clientes_unicos = len(set(v.cliente.cpf for v in vendas))
    receita_total = sum(v.valor_total for v in vendas)

    # Contagem exata de unidades vendidas por produto e por tipo
    contagem_produtos = {}
    quimio_vendidos = 0
    fito_vendidos = 0

    for venda in vendas:
        for prod in venda.produtos:
            contagem_produtos[prod.nome] = contagem_produtos.get(prod.nome, 0) + 1
            if prod.tipo_medicamento == "quimioterápico":
                quimio_vendidos += 1
            elif prod.tipo_medicamento == "fitoterápico":
                fito_vendidos += 1

    mais_vendido = max(contagem_produtos.items(), key=lambda item: item[1])

    print(f"• Total de vendas registradas:          {total_vendas}")
    print(f"• Pessoas atendidas (clientes únicos):  {clientes_unicos}")
    print(f"• Medicamento mais vendido:             {mais_vendido[0]} ({mais_vendido[1]} unidades)")
    print(f"• Remédios quimioterápicos vendidos:    {quimio_vendidos} unidades")
    print(f"• Remédios fitoterápicos vendidos:      {fito_vendidos} unidades")
    print(f"• Receita total apurada:                R${receita_total:.2f}")


# =====================================================================
# Menu Principal Interativo
# =====================================================================
def main():
    carregar_dados_iniciais()
    print("=" * 55)
    print("   🏥 SISTEMA DE GESTÃO DE DROGARIA (POO EM PYTHON)")
    print("=" * 55)
    print("Dados de demonstração carregados com sucesso!")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar cliente")
        print("2. Cadastrar medicamento")
        print("3. Realizar venda")
        print("4. Emitir relatórios")
        print("5. Sair")

        opcao = obter_opcao_inteira("Escolha uma opção: ")
        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            cadastrar_medicamento()
        elif opcao == 3:
            realizar_venda()
        elif opcao == 4:
            emitir_relatorios()
        elif opcao == 5:
            print("\nEncerrando sistema da Drogaria. Até logo!")
            break
        elif opcao is not None:
            print("[AVISO] Opção inválida. Digite um número de 1 a 5.")


if __name__ == "__main__":
    main()
