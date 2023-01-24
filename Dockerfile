FROM python:3.10
WORKDIR /ForwardCoverbot
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "echobot.py"]
