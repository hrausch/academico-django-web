# Informa a imagem base
FROM python:3
# Define o ambiente
ENV PYTHONUNBUFFERED=1
# Esta será o diretorio onde nosso projeto irá rodar
WORKDIR /code
# Copia o arquivo de dependências do projeto para o diretório
COPY requirements.txt /code/
# Instala as dependências do arquivo
RUN pip install -r requirements.txt
# Copia os arquivos da raiz para o diretório
COPY . /code/ 