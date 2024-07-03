# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required libraries
RUN apt-get update && \
    apt-get install -y gcc && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Compile the Cython file
RUN python setup.py build_ext --inplace

# Remove the original Python files
RUN rm -f main.pyx setup.py main.py Dockerfile requirements.txt
RUN find . -type f -name '*.c' -delete && \
    find . -type d -name '__pycache__' -exec rm -r {} +
RUN rm -rf build
# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "-c", "import main; main.app.run(host='0.0.0.0', port=5000)"]
