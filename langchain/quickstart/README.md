![image](https://github.com/Curt-Park/TIL/assets/14961526/ef26c913-e837-46ce-a8a9-57eb6e9824b1)

LangChain은 LLM application의 개발부터 배포, 모니터링까지 전반적인 life cycle을 구축하는 도구다.

## API Keys and Others

### For MAC
```bash
security add-generic-password -s 'openai.api-key' -a '' -w 'API-KEY'
security add-generic-password -s 'google.api-key' -a '' -w 'API-KEY'
security add-generic-password -s 'google.cse-id' -a '' -w 'CSE-ID'
```

### For Google Search
- Google API key: https://console.cloud.google.com/apis/credentials
- Google CSE ID: https://programmablesearchengine.google.com/controlpanel/overview
- Create Credentials: https://console.cloud.google.com/apis/api/customsearch.googleapis.com/


## Get OpenAI API Key
```bash
# bash
security find-generic-password -s 'openai.api-key' -w
security find-generic-password -s 'google.api-key' -w
security find-generic-password -s 'google.cse-id' -w
```

```python
# python script
import subprocess

os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'api-key.openai' -w", shell=True, text=True
).strip()
os.environ["GOOGLE_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'google.api-key' -w", shell=True, text=True
).strip()
os.environ["GOOGLE_CSE_ID"] = subprocess.check_output(
    "security find-generic-password -s 'google.cse-id' -w", shell=True, text=True
).strip()
```


## Setup
```bash
conda create -n langchain -y python=3.10
conda activate langchain
pip install requirements.txt
```

## Execution
```bash
$ python main.py
```

open http://localhost:8000/docs
<img width="1472" src="https://github.com/Curt-Park/TIL/assets/14961526/e9cc1091-b11e-4038-aaa0-4989d890c2fd">

## Test

#### Translator
```bash
$ curl -X 'POST' \
  'http://localhost:8000/translate/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {
    "language": "korean",
    "text": "this thing slaps!"
  }
}'

# response
{"output": "이거 진짜 좋아요!", ...}
```

#### Chatbot
```bash
$ curl -X 'POST' \
  --cookie "user_id=curt123;conversation_id=conv123" \
  'http://localhost:8000/chat/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {
    "text": "hi! my name is Curt"
  }
}'

# response
{"output": "Your name is Curt. How can I assist you" ...}


$ curl -X 'POST' \
  --cookie "user_id=curt123;conversation_id=conv123" \
  'http://localhost:8000/chat/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {
    "text": "what is my name?"
  }
}'

# response
{"output": "Your name is Curt. How can I assist you today?" ...}


$ curl -X 'POST' \
  --cookie "user_id=bob123;conversation_id=conv123" \
  'http://localhost:8000/chat/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {
    "text": "what is my name?"
  }
}'

# response
{"output": "I'm sorry, but I don't have access to personal information about you, including your name." ...}
```

#### Retriever
```bash
$ curl -X 'POST' \
  'http://localhost:8000/retriever/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "tell me about cats"
}'

# response
{"output": "Cats are independent pets that often enjoy their own space.", ...}
```


## Reference
#### Translator
- https://python.langchain.com/v0.2/docs/tutorials/llm_chain/
#### Chatbot
- https://python.langchain.com/v0.2/docs/tutorials/chatbot/
- https://github.com/langchain-ai/langserve/blob/main/examples/chat_with_persistence_and_user/server.py
#### Vector stores and retrievers
- https://python.langchain.com/v0.2/docs/tutorials/retrievers/
#### Search agent
- https://python.langchain.com/v0.2/docs/tutorials/agents/
