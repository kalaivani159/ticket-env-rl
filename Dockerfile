FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python inference.py && sleep 3600"]
