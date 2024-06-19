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
