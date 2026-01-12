FROM python:3.9-slim
WORKDIR /cooks
COPY . /cooks/
CMD ["python", "cooks.py"]