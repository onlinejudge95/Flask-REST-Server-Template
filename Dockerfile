FROM ubuntu:latest

RUN apt update -y && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.7 python3-pip

RUN mkdir -p /var/www/backend
WORKDIR /var/www/backend

COPY . .

RUN python3.7 -m pip install --no-cache-dir --upgrade pip setuptools pipenv && \
    pipenv install && \
    pipenv install --dev

CMD ["pipenv run gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "manage:app"]