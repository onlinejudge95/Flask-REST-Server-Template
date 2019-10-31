Flask-REST-Server-Template
==========================

[![Build Status](https://travis-ci.com/onlinejudge95/Flask-REST-Server-Template.svg?branch=master)](https://travis-ci.com/onlinejudge95/Flask-REST-Server-Template)
![GitHub top language](https://img.shields.io/github/languages/top/onlinejudge95/Flask-REST-Server-Template.svg)
[![codecov](https://codecov.io/gh/onlinejudge95/Flask-REST-Server-Template/branch/master/graph/badge.svg)](https://codecov.io/gh/onlinejudge95/Flask-REST-Server-Template)
[![Updates](https://pyup.io/repos/github/onlinejudge95/Flask-REST-Server-Template/shield.svg)](https://pyup.io/repos/github/onlinejudge95/Flask-REST-Server-Template/)
[![Python 3](https://pyup.io/repos/github/onlinejudge95/Flask-REST-Server-Template/python-3-shield.svg)](https://pyup.io/repos/github/onlinejudge95/Flask-REST-Server-Template/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/onlinejudge95/Github-Bot-Service.svg)
![GitHub issues](https://img.shields.io/github/issues/onlinejudge95/Flask-REST-Server-Template.svg)
![GitHub pull requests](https://img.shields.io/github/issues-pr/onlinejudge95/Flask-REST-Server-Template.svg)
![GitHub](https://img.shields.io/github/license/onlinejudge95/Flask-REST-Server-Template.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/onlinejudge95/Flask-REST-Server-Template.svg)

## Info
This is a template for spinning up a REST server in Flask for API first development.
Use this repo as a template repo.

## Dependencies
The server is tested in our travis account for following versions of Python
* 3.7

The server dependencies specified in `Pipfile`.

## Docker
The image is pushed to dockerhub {$LINK}, every push to git repository triggers a new build at the dockerhub.

* To build the image after modifications, run
  ```
  $ docker build -t {$IMAGE}:{$TAG} .
  ```
* To run the container after the image has build successfully, run
  ```
  $ docker run -it -d -p {$EXTERNAL_PORT}:8000 {$IMAGE}:{$TAG}
  ```

## Setup
To setup the dev env use the following commands.
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install --cache-dir .pip.cache/ --progress-bar emoji --upgrade pip setuptools
(env) $ pip install --cache-dir .pip.cache/ --progress-bar emoji --requirement requirements/dev.txt
(env) $ cp .env.example .env
```
To setup the db use the following commands.
```
(env) $ python manage.py db init
```
To make a migration run the folowing commands
```
(env) $ python manage.py db migrate -m $MESSAGE
(env) $ python manage.py db upgrade
```

## Contact
onlinejudge95
