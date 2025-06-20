## Used to test user-prompt-py
curl -i -X POST http://localhost:9999/api/v1/execute/demo/user-prompt \
    -H "Content-Type: multipart/form-data" \
    --form 'input.parameters={"modify":true,"enforce_user_prompt":"Remember to only mention cats in your response"};type=application/json' \
    --form 'metadata={};type=application/json' \
    --form 'input.messages={
    "messages": [
        {
        "content": "Do you like dogs?"
        }
    ]
    };type=application/json'