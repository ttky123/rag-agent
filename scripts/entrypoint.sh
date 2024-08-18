#!/bin/sh

# 테스트 시행
echo "Running tests..."
pytest 
TEST_RESULT=$?

# 테스트 통과 여부 확인
if [ $TEST_RESULT -ne 0 ]; then
  echo "Tests failed. Exiting."
  exit 1
else
  echo "Tests passed. Starting the app."
  exec uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
fi
