FROM python:2.7-alpine
MAINTAINER Felipe Santiago

RUN apk add --update libffi-dev gcc musl-dev make

RUN mkdir -p /src
ADD app /src/app
WORKDIR /src/app

ADD requirements.txt requirements.txt 

RUN pip install -r requirements.txt

CMD ["make run"]