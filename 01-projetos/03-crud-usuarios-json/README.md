# 📋 Sistema CRUD com Persistência em Arquivo JSON

Projeto prático desenvolvido no programa **Santander Coders** abordando **manipulação de arquivos, serialização de dados com JSON e operações de CRUD (Create, Read, Update, Delete)** em Python puro.

---

## 💡 Objetivos e Aprendizados

- Manipulação de arquivos com context managers (`with open(...)`).
- Serialização e desserialização de formatos estruturados com a biblioteca padrão `json` (`json.load` e `json.dump`).
- Implementação de um banco de dados leve baseado em documento sem dependências externas.
- **Padrão Soft Delete (Exclusão Lógica):** Em vez de remover fisicamente o registro da memória e do disco, mantemos o histórico alterando a flag `"Status": false`.
- Uso de empacotamento/desempacotamento de argumentos variáveis (`*ids`).

---

## 🗄️ Estrutura do Documento JSON (`usuarios_database.json`)

Cada registro é indexado pelo seu ID único sequencial:

```json
{
    "1": {
        "Status": true,
        "Nome": "Henrique",
        "Telefone": "78774123",
        "Endereço": "Rua do Python"
    },
    "4": {
        "Status": false,
        "Nome": "Maria",
        "Telefone": "74125823",
        "Endereço": "Av. Paulista"
    }
}
```

---

## 🚀 Como Executar

### Opção 1: Via Terminal (Script Interativo CLI)
```bash
cd 01-projetos/03-crud-usuarios-json
python main.py
```

### Opção 2: Via Jupyter Notebook
Abra o arquivo `sistema_crud_interativo.ipynb` no Jupyter Notebook, JupyterLab ou VS Code.

---

## 🛠️ Funcionalidades do Sistema

| Operação | Descrição |
| :--- | :--- |
| **1. Inserir usuário** | Cria um novo ID incremental ou reativa um cadastro inativo caso os dados coincidam. |
| **2. Excluir usuário** | Realiza a desativação lógica (`Status: False`) de um ou múltiplos IDs separados por vírgula. |
| **3. Atualizar usuário** | Menu interativo para alterar nome, telefone ou endereço individualmente. |
| **4. Consultar por ID** | Exibe detalhes cadastrais completos de um único registro. |
| **5. Listar usuários ativos** | Lista apenas registros com `Status: True`. |
| **6. Listar todos** | Permite auditoria exibindo tanto cadastros ativos quanto desativados. |
| **7. Salvar e Sair** | Garante a persistência em disco com indentação legível (`indent=4`). |
