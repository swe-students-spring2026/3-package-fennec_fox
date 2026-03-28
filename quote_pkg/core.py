import random
from data import quotes

def QuoteByCategory(category):
    matches =[
        quote["text"]
        for quote in quotes
        if quote["category"] == category
    ]
    if not matches:
        raise ValueError("Category not found")
    return random.choice(matches)

def QuoteRandom() -> str:

    if len(quotes) == 0:
        ValueError("quote list is empty")

    random_obj: object = random.choice(quotes)
    random_quote:str = random_obj["text"];

    if random_quote == None:
        ValueError("invalid quote object")

    if not isinstance(random_quote, str):
        ValueError("invalid quote text")

    return random_quote;