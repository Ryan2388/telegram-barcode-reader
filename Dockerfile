FROM python:3.7-stretch

RUN mkdir /app
ADD . /app/
WORKDIR /app

RUN DEBIAN_FRONTEND=noninteractive apt update && \
    DEBIAN_FRONTEND=noninteractive apt install libzbar0 -y
RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

ENV MODE polling
CMD python3 -m bot start-$MODE
