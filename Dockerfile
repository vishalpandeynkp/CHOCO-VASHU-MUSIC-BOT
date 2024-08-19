FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install system dependencies, including Tor
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ffmpeg \
       wget \
       tor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and install yt-dlp
RUN wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp \
    && chmod a+rx /usr/local/bin/yt-dlp \
    && yt-dlp -U

# Expose Tor SOCKS5 port
EXPOSE 9050 9051

# Configure Tor
RUN echo "SocksPort 0.0.0.0:9050" >> /etc/tor/torrc \
    && echo "ControlPort 9051" >> /etc/tor/torrc \
    && echo "CookieAuthentication 1" >> /etc/tor/torrc

# Copy application files
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Start Tor and your application
CMD ["bash", "-c", "tor & bash start"]
