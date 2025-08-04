FROM alpine/ansible:latest
WORKDIR /honeypot
COPY . .
ENTRYPOINT ["ansible-playbook", "-i", "inventory", "playbook.yml"]