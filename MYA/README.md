# ✨ Mya

Uma assistente virtual que está sendo desenvolvida usando Python, Gemini API e MySQL.

---

## 📖 Começando

Seguindo as instruções abaixo será possível executar

### 📝 Pré-requisitos

- python 3.10+
- MySQL
- Gemini API key

### 🔧Instalação

0. Caso não tenha git,python ou pip execute:

```bash
winget install Python.Python.3.14 Git.Git --silent --accept-source-agreements --accept-package-agreements
```

1. Clone o repositório

```bash
cd %USERPROFILE%\Documents
```

```bash
git clone https://github.com/FernandoBPontes16/Mya.git
```

2. Instale as depêndencias

```bash
cd Mya
```

```bash
pip install -r requirements.txt
```

3. Altere dados

Altere os dados do .env para utilização da Mya

Exemplo:

```env
GEMINI_API_KEY=your_api_key
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=your_database
```

4. Executar projeto

python app.py

## ⚒️ Ferramentas Utilizadas

- Python
- MySQL
- Gemini API
- python-dotenv
- mysql-connector-python
- openai

## 👤 Desenvolvedor

Projeto desenvolvido por Fernando Borba Pontes