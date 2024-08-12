# rag-agent
LLama 기반 RAG를 구현해보는 프로젝트입니다.
_____________________________________________________
rag-agent
├── app
│   ├── data
│   │   ├── api_spec.pdf
│   │   └── guide.pdf
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── llama_model.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── query_route.py
│   ├── services
│   │   ├── __init__.py
│   │   └── response_generator.py
│   ├── templates
│   │   └── index.html
│   └── utils
│       ├── document_loader.py
│       └── __init__.py
├── docker-compose.yml
├── dockerfile
├── dockerfile.test
├── entrypoint.sh
├── __init__.py
├── models
├── README.md
├── requirements.txt
├── scripts
│   └── entrypoint.sh
└── tests
    ├── __init__.py
    ├── test_api.py
    └── test_response_gen.py
___________________________________________________