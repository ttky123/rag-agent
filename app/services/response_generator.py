import logging
from models.llama_model import load_model
import asyncio

# Load model and tokenizer
model_id = 'MLP-KTLim/llama-3-Korean-Bllossom-8B-gguf-Q4_K_M'
model_path = 'models/MLP-KTLim-llama-3-Korean-Bllossom-8B-gguf-Q4_K_M/llama-3-Korean-Bllossom-8B-Q4_K_M.gguf'
tokenizer, model = load_model(model_id, model_path)
#
PROMPT = '''You are a helpful AI assistant. Please answer the user's questions kindly. 당신은 유능한 AI 어시스턴트입니다. 사용자의 질문에 대해 친절하게 답변해주세요.'''

async def generate_response(context, question):
    # 최대 토큰 수
    max_context_length = 8000  # 최대 문맥 길이 (입력용)
    max_output_tokens = 1024   # 최대 출력 토큰 수
    max_total_tokens = 512    # 모델의 전체 토큰 수 제한

    # 문맥을 토큰으로 변환하여 길이 조절
    context_tokens = tokenizer.encode(context)
    question_tokens = tokenizer.encode(question)
    prompt_tokens = tokenizer.encode(PROMPT)

    # 사용할 수 있는 문맥 길이 계산
    available_context_tokens = max_context_length - len(prompt_tokens) - len(question_tokens)

    # 문맥이 너무 길 경우 슬라이딩 윈도우 적용
    if len(context_tokens) > available_context_tokens:
        context_tokens = context_tokens[-available_context_tokens:]  # 최신 정보 유지를 위해 뒤에서 부터 자름

    # 최종 프롬프트 구성
    truncated_context = tokenizer.decode(context_tokens)
    prompt = f"{PROMPT}\nContext: {truncated_context}\nQuestion: {question}\nAnswer:"

    # 생성 옵션
    generation_kwargs = {
        "max_tokens": max_output_tokens,  # max token을 넘지 않기 위해 출력 토큰 수를 제한
        "stop": ["\n","\n\n"], 
        "top_p": 0.9,
        "temperature": 0.6,
    }

    # 생성
    try:
        loop = asyncio.get_event_loop()
        response_msg = await loop.run_in_executor(
            None,
            lambda: model(prompt, **generation_kwargs)
        )
        print("Response message: %s", response_msg)

        # 답변 후처리
        response_text = response_msg['choices'][0]['text'].strip()
        print("Generated text: %s", response_text)

        return response_text

    except Exception as e:
        logging.exception("Failed to generate response")
        return "An error occurred during response generation."

