# 🚀 Santander Coders — Portfólio de Engenharia de Dados & Python

Repositório estruturado contendo os projetos práticos, algoritmos resolvidos e materiais de consulta desenvolvidos ao longo do programa **Santander Coders** (formação promovida pelo **Banco Santander** em parceria com a **Ada Tech**).

O foco deste repositório é servir como **portfólio técnico profissional** e como **material de consulta e aprendizado** para outros estudantes e desenvolvedores interessados em Python moderno, Engenharia de Dados e Engenharia de Analytics.

---

## 📂 Estrutura do Repositório

```text
santander-coders-portfolio/
│
├── 01-projetos/
│   │
│   ├── 01-analytics-engineering-airbnb/   # 🏙️ Pipeline Medalhão (Bronze/Silver/Gold)
│   │   ├── pipeline_analytics_engineering.ipynb
│   │   ├── requirements.txt
│   │   ├── .env.example
│   │   └── README.md
│   │
│   ├── 02-sistema-drogaria-poo/           # 💊 Sistema em Programação Orientada a Objetos
│   │   ├── main.py
│   │   └── README.md
│   │
│   └── 03-crud-usuarios-json/             # 📋 Sistema CRUD com Persistência em JSON
│       ├── main.py
│       ├── sistema_crud_interativo.ipynb
│       ├── usuarios_database.json
│       └── README.md
│
├── 02-exercicios-resolvidos/              # 🧠 Desafios de Algoritmos & Testes Automatizados
│   ├── exercicios.py                      # Script com suíte de 8 testes automatizados
│   ├── exercicios_resolvidos_python.ipynb # Caderno interativo com explicações
│   └── README.md
│
├── 03-guia-de-estudos-python/             # 📖 Cheat Sheet e Consulta Rápida de Python
│   ├── guia_referencia_python.ipynb       # Caderno completo com teoria e exemplos
│   └── README.md
│
├── .gitignore
└── README.md
```

---

## 🌟 Destaques dos Projetos

### 1. [Pipeline de Analytics Engineering — Airbnb Rio de Janeiro](01-projetos/01-analytics-engineering-airbnb/)
Pipeline end-to-end implementando a **Arquitetura Medalhão** sobre dados reais do Inside Airbnb:
- **Camada Bronze:** Ingestão de dados brutos e carga estruturada em banco **PostgreSQL**.
- **Camada Silver:** Saneamento e tratamento de dados, NLP e limpeza textual com **spaCy**, verificação ortográfica e suíte de qualidade de dados com **Great Expectations**.
- **Camada Gold:** Modelagem dimensional e transformações analíticas agregadas via **dbt (Data Build Tool)**.

### 2. [Sistema de Gestão de Drogaria (POO em Python)](01-projetos/02-sistema-drogaria-poo/)
Aplicação em Python puro modelada com **Programação Orientada a Objetos**:
- Entidades desacopladas (`Medicamento`, `Cliente`, `Laboratorio`, `Venda`).
- Regras de negócio de retenção de receita para quimioterápicos e cálculos de descontos progressivos (idade > 65 anos e compras > R$ 150,00).
- Relatórios gerenciais e estatísticas diárias com agregação funcional.
- Contém dados de demonstração (*seed*) prontos para execução imediata.

### 3. [Sistema CRUD com Persistência em Arquivo JSON](01-projetos/03-crud-usuarios-json/)
Aplicação de gerenciamento cadastral demonstrando manipulação segura de arquivos:
- Operações completas de Create, Read, Update e Delete com serialização nativa em JSON.
- Implementação do padrão **Soft Delete** (exclusão lógica mantendo integridade histórica).
- Disponível tanto como script de linha de comando (`main.py`) quanto caderno interativo (`.ipynb`).

---

## 🧠 Exercícios Resolvidos & Algoritmos

Localizados em [`02-exercicios-resolvidos/`](02-exercicios-resolvidos/):
- **MapReduce:** Acumulação de operações com `map` e `functools.reduce`.
- **Funções de Alta Ordem:** Expressões `lambda` e predicados com `filter`.
- **Parsing e Leitura de Strings:** Processamento de dados tabulares delimitados sem bibliotecas externas.
- **Tratamento de Exceções:** Validações com blocos `try/except/else/finally` e lançamento defensivo de exceções.
- **Testes Unitários:** O arquivo `exercicios.py` inclui asserções automatizadas que validam todas as implementações.

---

## 🛠️ Tecnologias & Conceitos

- **Linguagens & Ambientes:** Python 3.10+, Jupyter Notebook, Git.
- **Engenharia de Dados & Bancos:** PostgreSQL, SQLAlchemy, Psycopg2, dbt Core.
- **Qualidade & Validação:** Great Expectations.
- **Processamento de Dados & NLP:** Pandas, NumPy, spaCy, PySpellChecker, BeautifulSoup.
- **Paradigmas:** Programação Orientada a Objetos (POO), Programação Funcional (FP), Modelagem Dimensional.

---

## ⚡ Como Clonar e Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/santander-coders-portfolio.git
cd santander-coders-portfolio

# 2. Para rodar a Drogaria em POO
python 01-projetos/02-sistema-drogaria-poo/main.py

# 3. Para rodar o CRUD JSON
python 01-projetos/03-crud-usuarios-json/main.py

# 4. Para rodar a suíte de testes dos exercícios
python 02-exercicios-resolvidos/exercicios.py
```

---

## 📜 Licença

Distribuído sob a licença [MIT](LICENSE). Sinta-se à vontade para utilizar como referência de estudos e projetos.
