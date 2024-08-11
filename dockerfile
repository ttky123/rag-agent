
FROM python:3.10-slim


RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    cmake \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt 
    # && pip install --no-cache-dir \
    # llama-cpp-python \
    # transformers \
    # fastapi \
    # uvicorn \
    # jinja2 \
    # pytest


RUN huggingface-cli login --token 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


RUN mkdir -p /models/MLP-KTLim-llama-3-Korean-Bllossom-8B-gguf-Q4_K_M


RUN if [ ! -f models/MLP-KTLim-llama-3-Korean-Bllossom-8B-gguf-Q4_K_M/config.json ]; then \
    huggingface-cli download MLP-KTLim/llama-3-Korean-Bllossom-8B-gguf-Q4_K_M --local-dir=models/MLP-KTLim-llama-3-Korean-Bllossom-8B-gguf-Q4_K_M --revision main; \
fi


COPY ./app /app
COPY ./tests /app/tests
COPY ./scripts/entrypoint.sh /app/entrypoint.sh

# 앱 실행 전 pyTest 실행을 위해 entrypoint 지정. 
RUN chmod +x /app/entrypoint.sh


EXPOSE 8000


ENTRYPOINT ["/app/entrypoint.sh"]

# # Use an official Python runtime as a parent image
# FROM python:3.10-slim

# # Install dependencies for building and compiling Rust extensions
# RUN apt-get update && apt-get install -y \
#     curl \
#     build-essential \
#     && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# # Add cargo to the path
# ENV PATH="/root/.cargo/bin:${PATH}"

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run app.py when the container launches
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
