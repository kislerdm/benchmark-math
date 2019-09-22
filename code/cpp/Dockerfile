FROM alpine:3.10 AS build

RUN apk add g++

WORKDIR /

COPY . .

RUN g++ -o runner bench.cpp

FROM alpine:3.10 AS serve

RUN apk add libstdc++

VOLUME /data

ENV REP=100

COPY --from=build /runner /runner

CMD i=0; while [ $i -lt 2 ]; do if [ $i -eq 0 ]; then ./runner > /data/cpp.txt; else ./runner >> /data/cpp.txt; fi; i=$(($i+1)); done