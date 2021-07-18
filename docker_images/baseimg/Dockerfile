FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt update && apt install python3 -yq

WORKDIR /app

COPY src .

CMD [ "/app/run.py" ]

