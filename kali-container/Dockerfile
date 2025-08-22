FROM kalilinux/kali-rolling:latest

# Install system packages
RUN apt-get update && \
    apt-get install -y \
    nmap \
    binutils \
    curl \
    dnsutils \
    git \
    nuclei \
    subfinder \
    python3-pip \
    python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment for Python packages
RUN python3 -m venv /root/venv
ENV PATH="/root/venv/bin:$PATH"

# Install Python packages in the virtual environment
RUN pip install --no-cache-dir \
    httpx \
    requests \
    holehe \
    ignorant

# Set working directory to /root
WORKDIR /root

# Start an interactive bash shell
CMD ["/bin/bash"]
