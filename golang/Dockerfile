FROM golang:1.18.2-buster

WORKDIR /app

COPY . /app

RUN go build -o build/fizzbuzz

CMD ["./build/fizzbuzz", "serve"]