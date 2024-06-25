![image](https://github.com/Curt-Park/TIL/assets/14961526/ef26c913-e837-46ce-a8a9-57eb6e9824b1)

LangChain은 LLM application의 개발부터 배포, 모니터링까지 전반적인 life cycle을 구축하는 도구다.

## Set OpenAI API Key
For MAC,
```bash
security add-generic-password -s 'api-key.openai' -a '' -w 'API-KEY'
```

## Get OpenAI API Key
```bash
# bash
security find-generic-password -s 'api-key.openai' -w
```

```python
# python script
import subprocess

os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'api-key.openai' -w",
    shell=True,
    text=True
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
translator:
```bash
$ curl -X 'POST' \
  'http://localhost:8000/translate/invoke' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {
    "language": "korean",
    "text": "this thing slaps!"
  },
  "config": {},
  "kwargs": {}
}'

# response
{
  "output": "이거 진짜 좋아요!",
  "metadata": {
    "run_id": "73b92825-2370-4b4f-a098-436b6d98f241",
    "feedback_tokens": []
  }
}
```

## Reference
- https://python.langchain.com/v0.2/docs/tutorials/llm_chain/
- https://python.langchain.com/v0.2/docs/tutorials/chatbot/
