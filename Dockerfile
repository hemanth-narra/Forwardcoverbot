FROM alpine:latest

# Install dependencies
RUN apk update && \
    apk add python3 py3-pip && \
    rm -rf /var/cache/apk/*

# Copy the application files
COPY requirements.txt /app/requirements.txt
COPY bot.py /app/bot.py

# Set the working directory
WORKDIR /app

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Run the application
CMD ["python3", "bot.py"]
