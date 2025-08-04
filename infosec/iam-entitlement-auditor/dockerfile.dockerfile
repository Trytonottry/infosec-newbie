FROM golang:1.22-alpine AS build
WORKDIR /src
COPY go.mod .
RUN go mod download
COPY . .
RUN go build -o auditor .

FROM alpine
COPY --from=build /src/auditor /usr/local/bin/auditor
ENTRYPOINT ["auditor"]