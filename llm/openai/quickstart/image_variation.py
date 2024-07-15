"""Image variation example (DALLE2).

References:
    - https://platform.openai.com/docs/guides/images/introduction?context=python
"""

import os

from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

with open("cat.png", "rb") as f:
    response = client.images.create_variation(model="dall-e-2", image=f, n=2, size="1024x1024")

print(response)
