import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt: str, model: str = "gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


# delimiters:
#  triple quotes: """"
#  triple backticks: ```
#  triple dashes: ---
#  angle brackets: <>
#  XML tags: <tag></tag>
def tactic_01():
    text = f"""
    You should express what you want a model to do by \ 
    providing instructions that are as clear and \ 
    specific as you can possibly make them. \ 
    This will guide the model towards the desired output, \ 
    and reduce the chances of receiving irrelevant \ 
    or incorrect responses. Don't confuse writing a \ 
    clear prompt with writing a short prompt. \ 
    In many cases, longer prompts provide more clarity \ 
    and context for the model, which can lead to \ 
    more detailed and relevant outputs.
    """
    prompt = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence.
    ```{text}```
    """
    response = get_completion(prompt)
    print("Tactic 01")
    print(response)
    print()


def tactic_02():
    text_1 = f"""
    Making a cup of tea is easy! First, you need to get some \ 
    water boiling. While that's happening, \ 
    grab a cup and put a tea bag in it. Once the water is \ 
    hot enough, just pour it over the tea bag. \ 
    Let it sit for a bit so the tea can steep. After a \ 
    few minutes, take out the tea bag. If you \ 
    like, you can add some sugar or milk to taste. \ 
    And that's it! You've got yourself a delicious \ 
    cup of tea to enjoy.
    """
    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"

    \"\"\"{text_1}\"\"\"
    """
    response = get_completion(prompt)
    print("Tactic 02")
    print("Completion for Text 1:")
    print(response)
    print()


def tactic_03():
    prompt = f"""
    Your task is to answer in a consistent style.

    <child>: Teach me about patience.

    <grandparent>: The river that carves the deepest \ 
    valley flows from a modest spring; the \ 
    grandest symphony originates from a single note; \ 
    the most intricate tapestry begins with a solitary thread.

    <child>: Teach me about resilience.
    """
    response = get_completion(prompt)
    print("Tactic 03")
    print(response)
    print()


def tactic_04():
    text = f"""
    In a charming village, siblings Jack and Jill set out on \ 
    a quest to fetch water from a hilltop \ 
    well. As they climbed, singing joyfully, misfortune \ 
    struck—Jack tripped on a stone and tumbled \ 
    down the hill, with Jill following suit. \ 
    Though slightly battered, the pair returned home to \ 
    comforting embraces. Despite the mishap, \ 
    their adventurous spirits remained undimmed, and they \ 
    continued exploring with delight.
    """
    # example 1
    prompt_1 = f"""
    Perform the following actions: 
    1 - Summarize the following text delimited by triple \
    backticks with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the following \
    keys: french_summary, num_names.

    Separate your answers with line breaks.

    Text:
    ```{text}```
    """
    response = get_completion(prompt_1)
    print("Tactic 04")
    print("Completion for prompt 1:")
    print(response)
    print()


def tactic_05():
    prompt = f"""
    Your task is to determine if the student's solution \
    is correct or not.
    To solve the problem do the following:
    - First, work out your own solution to the problem including the final total. 
    - Then compare your solution to the student's solution \ 
    and evaluate if the student's solution is correct or not. 
    Don't decide if the student's solution is correct until 
    you have done the problem yourself.

    Use the following format:
    Question:
    ```
    question here
    ```
    Student's solution:
    ```
    student's solution here
    ```
    Actual solution:
    ```
    steps to work out the solution and your solution here
    ```
    Is the student's solution the same as actual solution \
    just calculated:
    ```
    yes or no
    ```
    Student grade:
    ```
    correct or incorrect
    ```

    Question:
    ```
    I'm building a solar power installation and I need help \
    working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations \
    as a function of the number of square feet.
    ``` 
    Student's solution:
    ```
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    ```
    Actual solution:
    """
    print("Tactic 05")
    response = get_completion(prompt)
    print(response)
    print()


# tactic_01()
# tactic_02()
# tactic_03()
# tactic_04()
tactic_05()