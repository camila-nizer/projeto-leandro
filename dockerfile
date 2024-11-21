# Usar imagem base com Python 3.9
FROM python:3.9-slim

# Instalar dependências de sistema necessárias para o dlib, OpenCV e xvfb
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    libsm6 \
    libxext6 \
    xvfb \
    && apt-get clean

# Verificar se o grupo 'video' existe, caso contrário, criá-lo e adicionar o usuário
RUN groupadd -f -g 44 video && \
    useradd -m -u 1000 -g video myuser

# Instalar as dependências Python
RUN pip install --upgrade pip
RUN pip install opencv-python face_recognition

# Definir diretório de trabalho
WORKDIR /app

# Copiar o código para o contêiner
COPY app.py /app

# Ajustar permissões da pasta de capturas
RUN mkdir -p /app/saved_faces && chown -R myuser:video /app

# Alternar para o usuário criado
USER myuser

# Comando padrão para executar o script Python com xvfb
CMD ["sh", "-c", "xvfb-run -a python app.py"]
