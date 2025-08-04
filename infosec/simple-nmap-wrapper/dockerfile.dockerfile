FROM python:3.11-slim
RUN apt-get update && apt-get install -y nmap
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
ENTRYPOINT ["python", "nmap_wrapper.py"]