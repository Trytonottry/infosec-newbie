FROM ubuntu:20.04
RUN apt-get update && apt-get install -y gcc python3 python3-pip
RUN pip install pwntools
WORKDIR /work
COPY . .
RUN gcc -fno-stack-protector -no-pie -z execstack vuln.c -o vuln
CMD ["python3", "exploit.py"]