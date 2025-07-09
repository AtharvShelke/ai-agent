FROM python:latest


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

