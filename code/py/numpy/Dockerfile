FROM python:3.7.4-slim-stretch AS build

WORKDIR /

VOLUME /data

ENV REP=100

COPY . .

RUN python -m pip intall --no-cache-dir -r requirements.txt

CMD i=0; while [ $i -lt ${REP} ]; do if [ $i -eq 0 ]; then python bench_numpy.py > /data/py_numpy.txt; else python bench_numpy.py >> /data/py_numpy.txt; fi; i=$(($i+1)); done
