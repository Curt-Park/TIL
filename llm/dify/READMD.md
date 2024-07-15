# Dify

## Background
Flowise보다 Enterprise 사용에 더 적합한 도구 탐색. (e.g. Flowise는 계정 및 권한관리 기능 부재)
langflow와 dify가 물망에 오름.

- https://github.com/langflow-ai/langflow
- https://github.com/langgenius/dify

Langflow에 비해 Dify가 복잡한 의존관계를 가지고 있지만, 풍부한 기능을 제공함.

## Main Components
- api
- worker
- web

## Dependencies
- weaviate
- db (postgresql)
- redis
- nginx
- ssrf_proxy
- sandbox

## How to Run
```bash
docker compose up -d
```

Open http://localhost/

## How to Terminate
```bash
docker compose down
```

## References
- https://docs.dify.ai/
