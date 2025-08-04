FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY hibp.py .
ENTRYPOINT ["python", "hibp.py"]