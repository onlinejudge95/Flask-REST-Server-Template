FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y python3.7 python3.7-dev python3.7-venv python3-venv

RUN mkdir -p /var/www/backend
WORKDIR /var/www/backend

COPY . .

RUN python3.7 -m venv env && \
    ./env/bin/pip install --no-cache-dir --upgrade pip setuptools && \
    ./env/bin/pip install --no-cache-dir --progress-bar emoji --requirement requirements/prod.txt

CMD [ "env/bin/gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "manage:app" ]