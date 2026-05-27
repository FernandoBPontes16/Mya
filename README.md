# ✨ Mya

Uma assistente virtual que está sendo desenvolvida usando Python, Gemini API e MySQL.

---

## 📖 Começando

Seguindo as instruções abaixo será possível executar

### 📝 Pré-requisitos

- Windows
- Python 3.10+
- MySQL
- Gemini API Key
- Git

### 🔧Instalação

0. Caso não tenha git,python ou pip execute(opcional):

```bash
winget install Python.Python.3.14 Git.Git --silent --accept-source-agreements --accept-package-agreements
```

1. Clone o repositório

```bash
cd %USERPROFILE%\Documents
git clone https://github.com/FernandoBPontes16/Mya.git
cd Mya
```

2. Instale as dependências

```bash
pip install -r requirements.txt
```

3. Altere dados

Troque o nome de .env.example para .env e preencha os dados

Exemplo:

```env
GEMINI_API_KEY=your_api_key
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=your_database
```

4. Executar projeto
```bash
python app.py
```

## ⚒️ Ferramentas Utilizadas

- Python
- Gemini API
- MySQL
- google-genai
- mysql-connector-python
- python-dotenv
- openai`

## 🪛 Funções:

- Sistema simples de emoção
- Conversas com memoria
- Respostas utilizando stream
- Memoria com MySQL 
- Sistema de abrir aplicativos do PC

## 👤 Desenvolvedor

Projeto desenvolvido por Fernando Borba Pontes