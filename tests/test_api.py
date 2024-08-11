import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
os.environ["ENV"] = "test"
# TestClient 초기화
#client = TestClient(app, cookies={"session_id": "test-session-id"}, raise_server_exceptions=True)
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_ask_question():
    # 첫 번째 요청
    response = client.post("/ask", json={"question": "토큰이 중복 발급되면 어떻게 하나요?"})
    assert response.status_code == 200
    assert "answer" in response.json()

    # 추가 요청으로 멀티턴 시나리오 테스트
    response = client.post("/ask", json={"question": "그럼 대책은 무엇인가요?"})
    assert response.status_code == 200
    assert "answer" in response.json()

if __name__ == "__main__":
    pytest.main(["-s", __file__])
