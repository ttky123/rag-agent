
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
