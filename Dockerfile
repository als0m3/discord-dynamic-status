FROM python:3.6

COPY requirements* requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "main.py"]