# build stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

#installation of requirements into /root/.local
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# runtime stage
FROM python:3.11-slim

WORKDIR /app

# we copy installed dependencies from the builder stage to the runtime stage so that we safe space and there is no need to install again.
COPY --from=builder /root/.local /root/.local

# add binaries from /root/.local/bin to the PATH variable and keep the original values ($PATH)
ENV PATH=/root/.local/bin:$PATH

COPY app.py .

EXPOSE 5000

#listens on all IP and port 5000 
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

#create an image from powershell
# docker build -t my-flask-app .
#run the container
# docker run -p 5000:5000 my-flask-app


#Explanation
# -Dockerfile
# Uses multi-stage build to keep the final image small.
# Builder stage installs Python dependencies (Flask, Gunicorn) in a user directory.
# Runtime stage copies only the necessary dependencies and the app code.
# Exposes port 5000 and starts the app with Gunicorn for production-ready serving.
# -docker-compose.yml
# Defines a web service for the Flask app.
# Maps port 5000 from the container to the host for easy access.
# Automatically rebuilds the image and restarts the container if it stops.
# -requirements.txt
# Lists Python dependencies with exact versions for reproducibility.
# The Flask app is now running inside a container and accessible at:
# http://localhost:5000