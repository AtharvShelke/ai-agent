# declare what image to use
# FROM image_name:latest
FROM python:latest

WORKDIR /app

COPY ./src .



# docker build -f Dockerfile -t pyapp .
# docker run -it pyapp

# docker build -f Dockerfile -t atharv964/ai-test-app:latest .
# docker push atharv964/ai-test-app:latest
# docker pull atharv964/ai-py-app:latest
# docker run -it atharv964/ai-py-app:latest

# python -m http.server 8000
CMD ["python", "-m", "http.server", "8000"]

# docker run -it -p 8000:8000 pyapp

# after creating compose.yaml
# docker compose up
# docker compose down 
# if docker compose down is not used then for the next compose up use flag --remove-orphans

# docker compose build
# docker compose up --build for building and up the compose