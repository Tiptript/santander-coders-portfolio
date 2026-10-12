# 📖 Guia de Estudos e Consulta Rápida (Python Cheat Sheet)

Material de consulta rápida e revisão aprofundada de **Python Moderno**, cobrindo desde a sintaxe fundamental até técnicas funcionais e operações de persistência de dados.

---

## 🧭 Mapa de Tópicos do Caderno (`guia_referencia_python.ipynb`)

### 1. Coleções e Estruturas de Dados
- **Listas (`list`):** Fatiamento (*slicing*), ordenação *in-place* (`sort`) vs. cópia (`sorted`), inserções (`append`, `extend`), remoções (`pop`) e contagem (`count`).
- **Dicionários (`dict`):** Acesso seguro (`get`), iteração em chaves (`keys`), valores (`values`) e pares (`items`), mesclagem (`update`) e remoção (`pop`).
- **Conjuntos (`set`):** Operações matemáticas de conjuntos: união (`union` ou `|`), intersecção (`intersection` ou `&`), diferença (`difference` ou `-`) e diferença simétrica (`symmetric_difference`).
- **Tuplas (`tuple`):** Imutabilidade, estruturas ordenadas e desempacotamento de valores.
- **Geradores (`generator`):** Avaliação preguiçosa (*lazy evaluation*), uso da palavra-chave `yield` e expressões geradoras.

### 2. Manipulação Avançada de Strings
- Remoção de espaços e caracteres indesejados (`strip`, `lstrip`, `rstrip`).
- Divisão e partição com delimitadores (`split`).
- Junção eficiente de iteráveis de texto (`join`).
- Verificações de prefixo e sufixo (`startswith`, `endswith`) com suporte a tuplas de prefixos.
- Substituições parciais controladas (`replace`).

### 3. Funções e Modularização
- Declaração de funções com valores padrão (*default arguments*).
- Parâmetros nomeados (*keyword arguments*).
- Argumentos posicionais e nomeados variáveis: `*args` (tupla) e `**kwargs` (dicionário).
- Funções anônimas em linha (`lambda`).

### 4. Compreensões (Comprehensions)
- **List Comprehensions:** `[x for x in iter]` com filtros condicionais (`if`) e operadores ternários (`if/else`).
- **Dict Comprehensions:** `{k: v for ...}`.
- **Set Comprehensions:** `{x for ...}`.
- **Generator Expressions:** `(x for ...)`.

### 5. Programação Funcional
- **`map(funcao, iteravel)`:** Aplicação homogênea de transformação.
- **`filter(predicado, iteravel)`:** Seleção booleana de elementos.
- **`reduce(acumulador, iteravel)`:** Redução agregada de coleções (`functools.reduce`).

### 6. Tratamento de Exceções
- Estrutura completa: `try` -> `except` -> `else` -> `finally`.
- Captura seletiva de exceções específicas (*built-in exceptions*).

### 7. Manipulação de Arquivos e Serialização
- Gerenciamento de contexto com `with open(...)`.
- Modos de abertura: `r`, `w`, `a`, `x`, `+`, `b`.
- Serialização e desserialização de JSON: `json.dump`, `json.load`, `json.dumps`, `json.loads`.

---

## 🚀 Como Utilizar

Abra o caderno `guia_referencia_python.ipynb` no VS Code ou no Jupyter Notebook para visualizar as células de código explicativas com seus respectivos resultados.
