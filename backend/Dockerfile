FROM python:latest

# host.docker.internal is used to access the host machine from the container
# This is useful for development purposes, but not recommended for production
# curl -X POST -d '{"message": "Hello, world!"}' -H "Content-Type: application/json" http://host.docker.internal/chat/   
RUN apt-get update && apt-get install -y curl
# create python virtual environment
# isolate python from system level python
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# COPY LOCAL_FOLDER/FILE CONTAINER_FOLDER/FILE_DESTINATION
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY ./src .

CMD ["python", "-m", "http.server", "8000"]

