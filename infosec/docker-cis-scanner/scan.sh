scan.sh
```bash
#!/bin/sh
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  docker/docker-bench-security > report.html