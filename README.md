# RAG-Agent

## 프로젝트 소개

LLama 기반의 RAG(Retrieval-Augmented Generation) 시스템을 구현하는 프로젝트입니다. 마이데이터 도메인에 대한 질의 응답 기능을 수행합니다.

## 사용 기술

- **FastAPI** 
- **Faiss**
- **LangChain**
- **Torch**
- **Sentence-Transformers**
- **Pytest**

---

## 프로젝트 구조
rag-agent   
├── app   
│ ├── data   
│ │ ├── api_spec.pdf : API 명세서(데이터)   
│ │ └── guide.pdf : 가이드 문서(데이터)   
│ ├── init.py   
│ ├── main.py : FastAPI 앱       
│ ├── models   
│ │ ├── init.py   
│ │ └── llama_model.py : 모델 로드 및 초기화 코드      
│ ├── routes    
│ │ ├── init.py        
│ │ └── query_route.py : API 요청 경로 및 핸들러       
│ ├── services      
│ │ ├── init.py      
│ │ └── response_generator.py : 응답 생성 로직       
│ ├── templates      
│ │ └── index.html : 테스트용 웹페이지 탬플릿       
│ └── utils        
│ ├── init.py        
│ └── document_loader.py : Retrieval을 위한 문서 처리 util       
├── docker-compose.yml : Docker Compose 설정 파일       
├── Dockerfile : Docker 이미지 빌드 파일       
├── scripts       
│ └── entrypoint.sh : Pytest + Docker 컨테이너 시작 스크립트       
├── models : 모델을 저장하는 디렉토리        
├── README.md       
├── requirements.txt         
└── tests        
├── init.py       
├── test_api.py : API 테스트코드       
└── test_response_gen.py : 응답 생성 로직 테스트코드       
---

## 주요 모듈 설명

### app/models/llama_model.py

LLaMA 모델을 로드하고 초기화

### app/routes/query_route.py

사용자의 질문에 대한 API 요청을 처리. `/ask` 엔드포인트로 api 호출

### app/services/response_generator.py

RAG 로직을 수행하는 서비스

### app/utils/document_loader.py

PDF 형식의 문서를 로드하고 벡터화하여 임베딩 생성

### tests/

테스트 코드

---

## 실행 방법

### 사전 준비

- **Docker** , **Docker Compose**
- **Python 3.10+**
- **Nvidia GPU Driver + CUDA**

### 설치 및 실행
- docker-compose build
- docker-compose up
---
### 테스트 방법
http://localhost:48000 접속
