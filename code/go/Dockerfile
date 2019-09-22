FROM golang:1.11-alpine AS build

WORKDIR /

COPY . .

RUN go build -o runner bench.go

FROM alpine:3.10 AS serve

VOLUME /data

ENV REP=100

COPY --from=build /runner /runner

CMD i=0; while [ $i -lt ${REP} ]; do if [ $i -eq 0 ]; then ./runner > /data/go.txt; else ./runner >> /data/go.txt; fi; i=$(($i+1)); done