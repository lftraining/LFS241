FROM docker.io/golang:1.24
WORKDIR /go/src/lab-app/
COPY ./main.go .
RUN go mod init example.com && \
    go get github.com/prometheus/client_golang/prometheus && \
    go get github.com/prometheus/client_golang/prometheus/promhttp
EXPOSE 12345
CMD ["go", "run", "main.go"]