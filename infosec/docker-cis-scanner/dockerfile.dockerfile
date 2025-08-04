FROM alpine
RUN apk add --no-cache docker-cli
COPY scan.sh /usr/local/bin/scan
ENTRYPOINT ["scan"]