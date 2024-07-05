# OpenAI
GPT or else...

## Setup
```bash
conda create -n openai python=3.10
conda activate openai
pip install -r requirements.txt
```

## Website Crawler
```bash
python crawl_web.py --url https://huggingface.co/papers --max-depth 1 --must-include "/papers/"
```

## References
- https://platform.openai.com/docs/overview
