FROM cmnatic/subfinder-amass:latest
WORKDIR /app
COPY subrecon.py .
ENTRYPOINT ["python", "subrecon.py"]