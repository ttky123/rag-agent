import pytest
import logging
from app.services.response_generator import generate_response

logging.basicConfig(filename="test_results.log", level=logging.DEBUG)

@pytest.mark.asyncio
async def test_generate_response():
    context = "This is a test context."
    question = "What is this?"

    # 응답 생성 확인
    response = await generate_response(context, question)
    logging.info("response: " + response)

    assert isinstance(response, str)
    assert len(response) > 0

if __name__ == "__main__":
    pytest.main(["-s", __file__])
