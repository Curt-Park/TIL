# OpenAI
GPT or else...

## Setup
```bash
conda create -n openai python=3.10
conda activate openai
pip install -r requirements.txt
```

## How to use
```bash
python crawl_web.py --url https://huggingface.co/papers --max-depth 1 --must-include "/papers/"
python embed_text.py --text-dir parsed/huggingface.co
python main.py --embeddings embeddings/huggingface.co.csv
# Question?:
# 
# who are the authors of DisCo-Diff?
# 
# Answer:
#  The authors of DisCo-Diff are Yilun Xu, Gabriele Corso, Tommi Jaakkola, Arash Vahdat, and Karsten Kreis.
```

## References
- https://platform.openai.com/docs/overview
