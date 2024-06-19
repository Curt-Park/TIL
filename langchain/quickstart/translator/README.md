source: https://python.langchain.com/v0.2/docs/tutorials/llm_chain/


## Setup
```bash
conda create -n langchain -y python=3.10
conda activate langchain
pip install requirements.txt
```

## Execution
```bash
$ python translator.py
안녕하세요

$ python server.py
  __          ___      .__   __.   _______      _______. _______ .______     ____    ____  _______
 |  |        /   \     |  \ |  |  /  _____|    /       ||   ____||   _  \    \   \  /   / |   ____|
 |  |       /  ^  \    |   \|  | |  |  __     |   (----`|  |__   |  |_)  |    \   \/   /  |  |__
 |  |      /  /_\  \   |  . `  | |  | |_ |     \   \    |   __|  |      /      \      /   |   __|
 |  `----./  _____  \  |  |\   | |  |__| | .----)   |   |  |____ |  |\  \----.  \    /    |  |____
 |_______/__/     \__\ |__| \__|  \______| |_______/    |_______|| _| `._____|   \__/     |_______|

 LANGSERVE: Playground for chain "/chain/" is live at:
 LANGSERVE:  │
 LANGSERVE:  └──> /chain/playground/
 LANGSERVE:
 LANGSERVE: See all available routes at /docs/

 INFO:     Application startup complete.
 INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
 INFO:     ::1:53928 - "GET /docs HTTP/1.1" 200 OK
 INFO:     ::1:53928 - "GET /openapi.json HTTP/1.1" 200 OK
```

open http://localhost:8000/docs
<img width="1472" src="https://github.com/Curt-Park/TIL/assets/14961526/e9cc1091-b11e-4038-aaa0-4989d890c2fd">
