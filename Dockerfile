FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY count.txt ./count.txt

EXPOSE 5556

CMD ["python", "src/hello.py"]