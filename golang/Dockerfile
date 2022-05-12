# Stage 1

FROM golang:1.18.2-buster as build

WORKDIR /app

COPY . /app

RUN CGO_ENABLED=0 go build -o build/fizzbuzz

# Stage 2

FROM scratch

WORKDIR /app

COPY --from=build /app/templates/index.html ./templates/index.html

COPY --from=build /app/build/fizzbuzz ./fizzbuzz

ENTRYPOINT ["./fizzbuzz"]