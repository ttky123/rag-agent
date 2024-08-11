#!/bin/sh

# Run tests
echo "Running tests..."
pytest 
TEST_RESULT=$?

# Check if tests passed
if [ $TEST_RESULT -ne 0 ]; then
  echo "Tests failed. Exiting."
  exit 1
else
  echo "Tests passed. Starting the app."
  # Start the application
  exec uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
fi
