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

#TAILSCALE
FROM alpine:latest as tailscale
WORKDIR /app
ENV TSFILE=tailscale_1.36.1_amd64.tgz
RUN wget https://pkgs.tailscale.com/stable/${TSFILE} && \
  tar xzf ${TSFILE} --strip-components=1


# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
FROM alpine:latest
RUN apk update && apk add ca-certificates iptables ip6tables && rm -rf /var/cache/apk/*

# Copy binary to production image
COPY --from=builder /app/start.sh /app/start.sh
COPY --from=tailscale /app/tailscaled /app/tailscaled
COPY --from=tailscale /app/tailscale /app/tailscale
RUN mkdir -p /var/run/tailscale /var/cache/tailscale /var/lib/tailscale

# Run on container startup.
CMD ["/app/start.sh"]