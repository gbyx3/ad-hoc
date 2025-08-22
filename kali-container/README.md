# Kali Linux Custom Docker Image

This is a custom Kali Linux Docker image based on `kalilinux/kali-rolling:latest`, preinstalled with some tools for penetration testing and security research.

## Prerequisites
- Docker installed on your system.
- Basic familiarity with Docker commands.

## Getting Started

1. **Build the Docker Image**
   - Save the provided `Dockerfile` in your working directory.
   - Run the following command to build the image:
     ```bash
     docker pull kalilinux/kali-rolling:latest
     docker build -t kali-custom .
     ```

2. **Run the Container**
   - Use the following command to start the container with a custom hostname and a mounted volume:
     ```bash
     docker run --name "kali-container" --hostname "$(hostname -s)-kali" --rm -it -v $(pwd):/mnt kali-custom
     ```
   - **Explanation**:
     - `--name "kali-container"`: Names the container `kali-container`.
     - `--hostname "$(hostname -s)-kali"`: Sets the container's hostname to the short hostname of your host machine appended with `-kali`.
     - `--rm`: Automatically removes the container when it exits.
     - `-it`: Runs the container interactively with a terminal.
     - `-v $(pwd):/mnt`: Mounts the current working directory to `/mnt` in the container for file sharing.
     - `kali-custom`: The name of the built image.

3. **Access the Shell**
   - Once the container starts, you’ll be dropped into an interactive bash shell in the `/root` directory.
   - Run tools like `nmap`, `curl`, `holehe`, or others directly from the shell.

4. **Using Tools**
   - System tools (`nmap`, `binutils`, `curl`, `dnsutils`, `git`) are available globally.
   - Python tools (`httpx`, `requests`, `holehe`, `ignorant`) are installed in a virtual environment. The virtual environment is automatically activated (`/root/venv/bin` is in `PATH`).

5. **Exit the Container**
   - Type `exit` or press `Ctrl+D` to stop and remove the container (due to `--rm`).

## Notes
- The `/mnt` directory contains files from your host’s current working directory, allowing you to share files between the host and container.
- Persistent data in `/root` requires a Docker volume (e.g., `-v kali_data:/root`) if needed.
- Ensure your host’s Docker daemon is running before executing commands.
