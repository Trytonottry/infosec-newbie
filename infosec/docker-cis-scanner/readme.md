# 🐳 docker-cis-scanner  
Wrapper для docker-bench-security c HTML-отчётом.

## Run
```bash
docker build -t dscanner .
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock dscanner