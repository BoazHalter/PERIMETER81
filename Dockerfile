# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./echo-server.py /app/echo-server.py

# Install any needed packages specified in requirements.txt
# Since we only need requests, we can install it directly
RUN pip install requests

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variables
ENV ENVIRONMENT=development
RUN pwd
# Run echo_server.py when the container launches
CMD ["python", "./echo_server.py"]
