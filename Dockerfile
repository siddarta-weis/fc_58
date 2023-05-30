FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ARG DEBIAN_FRONTEND=noninteractive
ARG REQUIREMENTS

RUN useradd -ms /bin/bash python
USER python

WORKDIR /home/python/app

COPY ./${REQUIREMENTS} ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

CMD [ "tail", "-f", "/dev/null"]