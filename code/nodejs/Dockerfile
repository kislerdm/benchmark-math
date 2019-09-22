FROM node:12.8.0-alpine AS build

WORKDIR /

COPY . .

VOLUME /data

ENV REP=100

CMD i=0; while [ $i -lt ${REP} ]; do if [ $i -eq 0 ]; then node bench.js > /data/nodejs.txt; else node bench.js >> /data/nodejs.txt; fi; i=$(($i+1)); done