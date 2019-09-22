FROM python:3.7.4-slim-stretch AS build

WORKDIR /

VOLUME /data

ENV REP=100

COPY . .

CMD i=0; while [ $i -lt ${REP} ]; do if [ $i -eq 0 ]; then python bench.py > /data/py.txt; else python bench.py >> /data/py.txt; fi; i=$(($i+1)); done
