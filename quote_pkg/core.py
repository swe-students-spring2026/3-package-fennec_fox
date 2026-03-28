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