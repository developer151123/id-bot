FROM python:3.10
WORKDIR /app
COPY . .
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT ["python3", "./bot.py"]
