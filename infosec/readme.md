1.# 💥 bof-playground  
Классический buffer overflow с эксплойтом pwntools.

## Run
```bash
docker build -t bof .
docker run --rm bof

2.# 🐄 cowrie-quickstart  
SSH-honeypot Cowrie в одной команде.

## Usage
```bash
docker compose up -d
# логины в ./outputs/

3.# 🐳 docker-cis-scanner  
Wrapper для docker-bench-security c HTML-отчётом.

## Run
```bash
docker build -t dscanner .
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock dscanner

4.# 💥 exploit-dev-playground  
5 упрощённых CVE с PoC и эксплойтами.

## Build & Run
```bash
docker build -t playground .
docker run --rm -it playground

5.# 🎣 gophish-sandbox  
One-line Gophish для тестов фишинга.

## Start
```bash
docker compose up -d
# админка https://localhost:3333
# login: admin / gophish

6.# 🔍 hibp-checker  
CLI-скрипт для проверки e-mail в Have I Been Pwned.

## Run
```bash
docker run --rm -e HIBP_KEY=xxx hibp user@example.com

7.# 🏠 home-elk-lab  
Docker Compose стек ELK для сбора Syslog и анализа SSH brute-force.

## Usage
```bash
docker compose up -d
# отправьте лог на 127.0.0.1:5140/UDP
# откройте http://localhost:5601

8.# 🐄 honeypot-farm  
Ansible-роли для поднятия Cowrie, Dionaea, T-Pot в AWS/VMware.

## Usage
```bash
docker compose run --rm deploy

9.# 🔍 iam-entitlement-auditor  
CLI-утилита на Go для аудита прав в AWS IAM.

## Run
```bash
docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY ghcr.io/you/auditor

10.# 📡 mdr-connector  
Webhook proxy: TheHive/MISP → Slack/Teams.

## Setup
```bash
cp .env.example .env
# add SLACK_URL
docker compose up

11.# 🧾 sigma-starter-pack  
3 базовых Sigma-правила для новичков.

## Validate
```bash
sigma check sigma/

12.# 🗺️ simple-nmap-wrapper  
CLI-обёртка над nmap, выводит таблицу открытых портов.

## Run
```bash
docker build -t nwrap .
docker run --rm nwrap 127.0.0.1

13.# 🔍 sub-recon-tool  
Сбор поддоменов subfinder + amass + A-записи.

## Run
```bash
docker build -t subr .
docker run --rm subr example.com

14.# 📡 wifi-forensics-lab  
Vagrant-стенд для захвата 4-Way Handshake и взлома пароля.

## Quick start
```bash
vagrant up
vagrant ssh
# inside VM: sudo airodump-ng wlan0mon ...
