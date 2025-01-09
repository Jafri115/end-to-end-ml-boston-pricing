# Use the official Python 3.7 image as the base image
FROM python:3.7

# Copy the current directory (your app code and files) into the /app directory in the Docker container
COPY . /app

# Set the working directory inside the container to /app
WORKDIR /app

# Install the required Python dependencies listed in requirements.txt
# The --no-cache-dir option prevents caching of package files, reducing the image size
RUN pip install -r requirements.txt

# Expose the port that the app will listen on
# Heroku dynamically assigns a $PORT, so we expose this environment variable
EXPOSE $PORT

# Define the command to start the app using Gunicorn with 4 worker processes
# Gunicorn is a production-grade WSGI server for Python web apps
# CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app:
#     This starts the application using Gunicorn, a production-ready web server.
#     --workers=4 specifies the number of worker processes for handling requests (can be adjusted based on your app's expected traffic and server resources).
#     --bind 0.0.0.0:$PORT binds the server to all available network interfaces on the assigned port.
#     app:app points to the Flask app object, where the first app is the Python filename (app.py) and the second app is the Flask app instance within the file.
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app