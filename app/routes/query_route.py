import os
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from services.response_generator import generate_response
from utils.document_loader import load_documents
import logging
import uuid

router = APIRouter()

class Query(BaseModel):
    question: str

vectorstore = load_documents()
#middleware를 사용하여 멀티텀 기능 구현
@router.post("/ask")
async def ask_question(request: Request, query: Query):
    try:
        if os.getenv("ENV") != "test":
            # 새로운 클라이언트가 접속할 경우 UUID 생성
            if "session_id" not in request.session:
                request.session["session_id"] = str(uuid.uuid4())

            # 세션에서 이전 대화 문맥 가져오기
            previous_context = request.session.get("context", "")
        else:
            # 테스트 환경에서는 세션을 사용하지 않음
            previous_context = ""

        # context를 300자로 요약
        max_context_length = 300  # 원하는 최대 문맥 길이 (토큰 수로 조정 필요)
        if len(previous_context) > max_context_length:
            previous_context = previous_context[-max_context_length:]  # 최근 내용만 유지(max_token을 넘지 않기 위해)

        # 현재 질문을 문맥에 추가
        full_context = f"{previous_context}\nUser: {query.question}"

        # 유관한 document retrieve
        retriever = vectorstore.as_retriever()
        docs = retriever.invoke(query.question)
        # 검색된 문서에서 내용 추출.
        context = docs[0].page_content if docs else ""
        
        # 전체 context와 검색된 내용을 결합
        combined_context = f"{context}\n{full_context}"

        # 비동기 모델 인퍼런스 수행
        result = await generate_response(combined_context, query.question)

        if os.getenv("ENV") != "test":
            # 세션에 새로운 context 저장
            request.session["context"] = f"{full_context}\nAssistant: {result}"

        return {"answer": result}
    except Exception as e:
        logging.exception("Exception occurred during generation: " + str(e))
        raise HTTPException(status_code=500, detail=str(e))


# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from services.response_generator import generate_response
# from utils.document_loader import load_documents
# import logging
# import uuid
# router = APIRouter()


# class Query(BaseModel):
#     question : str
    
    
# vectorstore= load_documents()


# @router.post("/ask")
# async def ask_question(query: Query):
#     try:
#         # Use invoke to retrieve documents
#         retriever = vectorstore.as_retriever()
#         docs = retriever.invoke(query.question)
#         context = docs[0].page_content if docs else ""

#         result = await generate_response(context,query.question)
#         return{"answer" : result}
    
#     except Exception as e:
#         logging.exception("Exception Occured during generation" + {str(e)})
#         raise HTTPException(status_code=500, detail = str(e))