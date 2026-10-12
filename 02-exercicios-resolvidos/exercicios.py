"""
Exercícios Resolvidos de Lógica de Programação, Algoritmos e Programação Funcional
Santander Coders - Ada Tech

Este script reúne a resolução comentada e com testes automatizados
dos principais exercícios práticos cobrados nas listas e avaliações.
"""

from functools import reduce
import json
from typing import List, Dict, Union, Any


# =====================================================================
# 1. Processamento e Manipulação de Dados em Strings / CSV
# =====================================================================

def produto_mais_vendido(vendas_str: str) -> str:
    """
    Lê uma string simulando um arquivo CSV com separador ', '
    (colunas: data, produto, quantidade, valor) e retorna o nome do
    produto com a maior quantidade de unidades vendidas.
    """
    linhas = [l.strip() for l in vendas_str.strip().split("\n") if l.strip()]
    if len(linhas) <= 1:
        return ""

    # Dicionário acumulador de quantidades por produto
    vendas_por_produto: Dict[str, int] = {}
    for linha in linhas[1:]:
        partes = [p.strip() for p in linha.split(",")]
        if len(partes) >= 3:
            nome_produto = partes[1]
            quantidade = int(partes[2])
            vendas_por_produto[nome_produto] = vendas_por_produto.get(nome_produto, 0) + quantidade

    # Retorna o produto com maior volume vendido
    return max(vendas_por_produto.items(), key=lambda x: x[1])[0]


def media_vendas(vendas_str: str) -> float:
    """
    Calcula o valor financeiro total de vendas a partir de um CSV em string
    multiplicando quantidade * preço unitário de cada item registrado.
    """
    linhas = [l.strip() for l in vendas_str.strip().split("\n") if l.strip()]
    if len(linhas) <= 1:
        return 0.0

    total = 0.0
    for linha in linhas[1:]:
        partes = [p.strip() for p in linha.split(",")]
        if len(partes) >= 4:
            quantidade = float(partes[2])
            preco_unitario = float(partes[3])
            total += quantidade * preco_unitario

    return round(total, 2)


# =====================================================================
# 2. Programação Funcional (Map, Filter, Reduce, Lambda)
# =====================================================================

def ger_reduce(numeros: List[Union[int, float]]) -> Union[int, float]:
    """
    Calcula a soma dos quadrados dos elementos de uma lista numérica
    utilizando o paradigma funcional (map + reduce).
    Exemplo: [1, 2, 3, 4] -> 1² + 2² + 3² + 4² = 30
    """
    if not numeros:
        return 0
    quadrados = map(lambda x: x ** 2, numeros)
    return reduce(lambda acumulador, valor: acumulador + valor, quadrados)


def div2(numeros: List[int]) -> List[int]:
    """
    Filtra uma lista de números inteiros mantendo apenas os números pares
    utilizando a função de alta ordem `filter` e uma função anônima `lambda`.
    """
    return list(filter(lambda x: x % 2 == 0, numeros))


# =====================================================================
# 3. Compreensão de Listas, Conjuntos e Dicionários
# =====================================================================

def numeros_div_7(lista: List[int]) -> List[int]:
    """
    Recebe uma lista de inteiros e retorna uma nova lista ordenada
    contendo apenas os elementos únicos divisíveis por 7.
    """
    elementos_unicos = set(lista)
    divisiveis = [x for x in elementos_unicos if x % 7 == 0]
    return sorted(divisiveis)


def cria_arquivo_json(chaves: List[str], valores: List[Any]) -> str:
    """
    Combina duas listas (chaves e valores) em um dicionário
    e retorna sua representação serializada em formato JSON.
    """
    if len(chaves) != len(valores):
        raise ValueError("A quantidade de chaves e valores deve ser idêntica.")
    dicionario = dict(zip(chaves, valores))
    return json.dumps(dicionario, ensure_ascii=False)


def contar_frequencia_caracteres(texto: str) -> Dict[str, int]:
    """
    Retorna a contagem de frequência de cada caractere de uma string
    (conceito base para bag-of-words em PLN).
    """
    frequencias: Dict[str, int] = {}
    for char in texto:
        frequencias[char] = frequencias.get(char, 0) + 1
    return frequencias


def gerar_dicionario_fatoriais(k: int) -> Dict[int, int]:
    """
    Gera um dicionário mapeando cada número de 1 até k ao seu respectivo fatorial.
    Exemplo para k=4: {1: 1, 2: 2, 3: 6, 4: 24}
    """
    resultado = {}
    fatorial = 1
    for i in range(1, k + 1):
        fatorial *= i
        resultado[i] = fatorial
    return resultado


# =====================================================================
# 4. Tratamento de Exceções e Validações
# =====================================================================

def verifica_numero_positivo(numero: Union[int, float]):
    """
    Verifica se o número é maior que zero; lança Exception caso contrário.
    """
    if numero <= 0:
        raise ValueError("Número deverá ser maior que zero")
    return True


def divide_dois_numeros(x: Any, y: Any) -> float:
    """
    Divide x por y tratando divisões por zero e tipos inválidos.
    """
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    except TypeError:
        raise TypeError("Ambos os argumentos precisam ser números válidos.")


# =====================================================================
# Suíte de Testes Automatizados
# =====================================================================

def executar_testes():
    print("=" * 60)
    print("   Executando testes automatizados dos exercícios...")
    print("=" * 60)

    # Teste 1: Produto mais vendido
    dados_vendas = (
        "data, produto, quantidade, valor\n"
        "20/10/2022, prato, 5, 20.00\n"
        "19/10/2022, copo, 15, 5.00\n"
        "07/07/2022, lampada, 3, 68.90\n"
        "10/08/2022, copo, 2, 5.00"
    )
    assert produto_mais_vendido(dados_vendas) == "copo", "Erro no produto mais vendido"
    print("[OK] produto_mais_vendido")

    # Teste 2: Média / Total de vendas
    dados_totais = (
        "data, produto, quantidade, valor\n"
        "20/10/2022, ventilador, 1, 120.00\n"
        "19/10/2022, cadeira, 1, 335.55\n"
        "07/07/2022, lampada, 3, 68.90"
    )
    # 120 + 335.55 + (3 * 68.90 = 206.70) = 662.25
    assert media_vendas(dados_totais) == 662.25, "Erro no cálculo de total de vendas"
    print("[OK] media_vendas")

    # Teste 3: MapReduce (Soma dos quadrados)
    assert ger_reduce([1, 2, 3, 4]) == 30, "Erro no ger_reduce (1+4+9+16=30)"
    assert ger_reduce([0, -2, 5]) == 29, "Erro no ger_reduce com números negativos"
    print("[OK] ger_reduce (MapReduce)")

    # Teste 4: Filter com pares
    assert div2([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8], "Erro no div2"
    print("[OK] div2 (Filter com Lambda)")

    # Teste 5: Divisíveis por 7 únicos e ordenados
    lista_desordenada = [14, 7, 21, 14, 3, 5, 28, 7, 49, 10]
    assert numeros_div_7(lista_desordenada) == [7, 14, 21, 28, 49], "Erro no numeros_div_7"
    print("[OK] numeros_div_7 (Compreensão + Set)")

    # Teste 6: Criação de JSON a partir de listas
    json_result = cria_arquivo_json(["modulo", "curso"], [2, "Santander Coders"])
    d = json.loads(json_result)
    assert d == {"modulo": 2, "curso": "Santander Coders"}, "Erro no cria_arquivo_json"
    print("[OK] cria_arquivo_json")

    # Teste 7: Fatoriais
    assert gerar_dicionario_fatoriais(4) == {1: 1, 2: 2, 3: 6, 4: 24}, "Erro nos fatoriais"
    print("[OK] gerar_dicionario_fatoriais")

    # Teste 8: Validação e tratamento de erros
    try:
        divide_dois_numeros(10, 0)
        assert False, "Deveria ter lançado ZeroDivisionError"
    except ZeroDivisionError:
        pass

    try:
        divide_dois_numeros(10, "invalido")
        assert False, "Deveria ter lançado TypeError"
    except TypeError:
        pass
    print("[OK] divide_dois_numeros (Exceções capturadas com sucesso)")

    print("=" * 60)
    print("Sucesso: Todos os 8 testes unitários passaram perfeitamente!")
    print("=" * 60)


if __name__ == "__main__":
    executar_testes()
