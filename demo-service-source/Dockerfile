FROM docker.io/golang:1.24-alpine AS builder
WORKDIR /source
COPY . /source
RUN go mod download
RUN go build -v -o prometheus_demo_service .

FROM docker.io/alpine:3
COPY --from=builder /source/prometheus_demo_service  /bin/prometheus_demo_service
EXPOSE 8080
ENTRYPOINT ["/bin/prometheus_demo_service"]