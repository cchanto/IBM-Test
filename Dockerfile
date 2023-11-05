# Use a more common version of Ubuntu and a specific version of nginx
FROM ubuntu:20.04

# Add labels for metadata
LABEL maintainer="chantoc.chanto@gmail.com"

# Set timezone to avoid interactive prompt
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime

# Combine RUN commands and install necessary tools
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl nginx git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create necessary directory structure
RUN mkdir -p /var/www/html/css

# Fetch the files using curl
RUN curl -o /var/www/html/index.html "https://www.random.org/strings/?num=10&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new" \
    && curl -o /var/www/html/css/style.css "https://www.random.org/css/style.css"

# Expose port 80
EXPOSE 80

# Set up the CMD
CMD ["nginx", "-g", "daemon off;"]
