# rag-agent
LLama 기반 RAG를 구현해보는 프로젝트입니다.

rag-agent <br/>
├── app <br/>
│   ├── data <br/>
│   │   ├── api_spec.pdf <br/>
│   │   └── guide.pdf <br/>
│   ├── __init__.py <br/>
│   ├── main.py <br/>
│   ├── models <br/>
│   │   ├── __init__.py <br/>
│   │   └── llama_model.py <br/>
│   ├── routes <br/>
│   │   ├── __init__.py <br/>
│   │   └── query_route.py <br/>
│   ├── services <br/>
│   │   ├── __init__.py <br/>
│   │   └── response_generator.py <br/>
│   ├── templates <br/>
│   │   └── index.html <br/>
│   └── utils <br/>
│       ├── document_loader.py <br/>
│       └── __init__.py <br/>
├── docker-compose.yml <br/>
├── dockerfile <br/>
├── dockerfile.test <br/>
├── entrypoint.sh <br/>
├── __init__.py <br/>
├── models <br/>
├── README.md <br/>
├── requirements.txt <br/>
├── scripts <br/>
│   └── entrypoint.sh <br/>
└── tests <br/>
    ├── __init__.py <br/>
    ├── test_api.py <br/>
    └── test_response_gen.py <br/>
