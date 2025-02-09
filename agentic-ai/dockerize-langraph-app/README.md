### Réfs: 
- [Youtube video](https://youtu.be/3o4mAJhT2HY?si=rqTJCKL6_qM1q3sh)

# Docker CLI Commands

## Building the Docker Image
```sh
docker build -t langgraph-agent-app .
```
### Explanation:
- `docker build`: Creates a Docker image from a Dockerfile.
- `-t langgraph-agent-app`: Tags the image with a name (`langgraph-agent-app`). If no tag is provided, `latest` is used by default (`langgraph-agent-app:latest`).
- `.`: Specifies the current directory where the Dockerfile is located.

## Running the Docker Container with Environment Variables
```sh
docker run -d -p 8000:8000 -p 8501:8501 \
  -e GROQ_API_KEY=your_groq_api_key \
  -e TAVILY_API_KEY=your_tavily_api_key \
  --name langgraph-agent-container langgraph-agent-app
```
### Explanation:
- `docker run`: Creates and starts a container from a Docker image.
- `-d`: Runs the container in detached mode (background execution).
- `-p 8000:8000`: Maps the container's port 8000 (FastAPI) to the host machine.
- `-p 8501:8501`: Maps the container's port 8501 (Streamlit UI) to the host machine.
- `-e GROQ_API_KEY=your_groq_api_key`: Sets the `GROQ_API_KEY` environment variable inside the container.
- `-e TAVILY_API_KEY=your_tavily_api_key`: Sets the `TAVILY_API_KEY` environment variable inside the container.
- `--name langgraph-agent-container`: Assigns a custom name to the container for easy management.
- `langgraph-agent-app`: Specifies the Docker image to use.

## Pushing the Docker Image to Docker Hub
### Log in to Docker Hub
```sh
docker login
```
### Tag the Image
```sh
docker tag langgraph-agent-app your_dockerhub_username/langgraph-agent-app:latest
```
### Push the Image
```sh
docker push your_dockerhub_username/langgraph-agent-app:latest
```
### Explanation:
- `docker tag`: Assigns a new tag to the image to match your Docker Hub repository.
- `docker push`: Uploads the image to Docker Hub.

## Pulling the Image from Docker Hub
```sh
docker pull your_dockerhub_username/langgraph-agent-app:latest
```
### Explanation:
- `docker pull`: Downloads the image from Docker Hub to the local machine.

## Running the Pulled Image
```sh
docker run -d -p 8000:8000 -p 8501:8501 \
  -e GROQ_API_KEY=your_groq_api_key \
  -e TAVILY_API_KEY=your_tavily_api_key \
  --name langgraph-agent-container your_dockerhub_username/langgraph-agent-app:latest
```

