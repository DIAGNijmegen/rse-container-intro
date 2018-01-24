FROM python:3.6
MAINTAINER james <james.meakin@radboudumc.nl>

RUN mkdir /www/
WORKDIR /www/

COPY webapp.py /www/

RUN pip install sanic

ENTRYPOINT ["python","-m","webapp"]

