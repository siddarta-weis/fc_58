FROM python:3.11-slim

RUN useradd -ms /bin/bash python
USER python
WORKDIR /home/python/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

RUN apt update && \
    apt install -y openjdk-11-jre

CMD [ "tail", "-f", "/dev/null"]