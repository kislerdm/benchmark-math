FROM r-base:3.6.1 AS build

WORKDIR /

VOLUME /data

ENV REP=100

COPY . .

CMD i=0; while [ $i -lt ${REP} ]; do if [ $i -eq 0 ]; then Rscript bench.R > /data/r.txt; else Rscript bench.R >> /data/r.txt; fi; i=$(($i+1)); done