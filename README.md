Here's the updated `README.md` file with instructions on how to build and run the Docker container, including running it with the name `text-extractor` and ensuring it restarts always.

### `README.md`

```markdown
# Text Extractor API

This application extracts text from PDF, DOCX, and TXT files and splits the text into chunks of a specified size.

## Running the Application

### Requirements

- Docker

### Building the Docker Image

Navigate to the `app` directory:

```sh
cd ~/text_extractor/app
```

Build the Docker image:

```sh
sudo docker build -t text_extractor .
```

### Running the Docker Container

Run the Docker container with the name `text-extractor` and ensure it restarts always:

```sh
sudo docker run -d --name text-extractor -p 5000:5000 --restart always text_extractor
```

### Using the API

Send a POST request to `http://localhost:5000/extract` with a file and chunk size.

#### Example using `curl`

```sh
curl -X POST -F "file=@path_to_your_file.pdf" -F "chunk_size=100" http://localhost:5000/extract
```

#### Example using Python `requests`

```python
import requests

url = 'http://localhost:5000/extract'
file_path = 'path_to_your_file.pdf'
chunk_size = 100

files = {'file': open(file_path, 'rb')}
data = {'chunk_size': chunk_size}

response = requests.post(url, files=files, data=data)
print(response.json())
```

### Development and Testing

If you want to run the application locally for development and testing:

1. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

2. Run the Flask application:

    ```sh
    python main.py
    ```

The API will be available at `http://localhost:5000/extract`.
```

This `README.md` file now includes detailed instructions on how to build the Docker image, run the Docker container with the specified name and restart policy, and use the API.
