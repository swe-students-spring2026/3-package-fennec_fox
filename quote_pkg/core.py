import random

quotes = [
    {"text": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney", "category": "motivational", "emotion": "inspired"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt", "category": "motivational", "emotion": "hopeful"},
    {"text": "It always seems impossible until it's done.", "author": "Nelson Mandela", "category": "motivational", "emotion": "determined"},
    {"text": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt", "category": "motivational", "emotion": "focused"},
    {"text": "Act as if what you do makes a difference. It does.", "author": "William James", "category": "motivational", "emotion": "inspired"},
    {"text": "I think, therefore I am.", "author": "René Descartes", "category": "historical", "emotion": "thoughtful"},
    {"text": "That which does not kill us makes us stronger.", "author": "Friedrich Nietzsche", "category": "historical", "emotion": "resilient"},
    {"text": "The only thing we have to fear is fear itself.", "author": "Franklin D. Roosevelt", "category": "historical", "emotion": "confident"},
    {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein", "category": "historical", "emotion": "hopeful"},
    {"text": "Government of the people, by the people, for the people, shall not perish.", "author": "Abraham Lincoln", "category": "historical", "emotion": "serious"},
    {"text": "I'm not arguing, I'm just explaining why I'm right.", "author": "Unknown", "category": "funny", "emotion": "playful"},
    {"text": "People say nothing is impossible, but I do nothing every day.", "author": "A. A. Milne", "category": "funny", "emotion": "playful"},
    {"text": "Behind every great man is a woman rolling her eyes.", "author": "Jim Carrey", "category": "funny", "emotion": "sarcastic"},
    {"text": "If you think you are too small to make a difference, try sleeping with a mosquito.", "author": "Dalai Lama", "category": "funny", "emotion": "light"},
    {"text": "Get your facts first, then you can distort them as you please.", "author": "Mark Twain", "category": "funny", "emotion": "witty"},
    {"text": "The unexamined life is not worth living.", "author": "Socrates", "category": "reflective", "emotion": "thoughtful"},
    {"text": "To be, or not to be: that is the question.", "author": "William Shakespeare", "category": "reflective", "emotion": "contemplative"},
    {"text": "Happiness depends upon ourselves.", "author": "Aristotle", "category": "reflective", "emotion": "calm"},
    {"text": "Turn your wounds into wisdom.", "author": "Oprah Winfrey", "category": "reflective", "emotion": "healing"},
    {"text": "Knowing yourself is the beginning of all wisdom.", "author": "Aristotle", "category": "reflective", "emotion": "thoughtful"},
    {"text": "No act of kindness, no matter how small, is ever wasted.", "author": "Aesop", "category": "kindness", "emotion": "warm"},
    {"text": "Kindness is a language which the deaf can hear and the blind can see.", "author": "Mark Twain", "category": "kindness", "emotion": "warm"},
    {"text": "Wherever there is a human being, there is an opportunity for a kindness.", "author": "Lucius Annaeus Seneca", "category": "kindness", "emotion": "compassionate"},
    {"text": "Carry out a random act of kindness, with no expectation of reward.", "author": "Princess Diana", "category": "kindness", "emotion": "kind"},
    {"text": "A warm smile is the universal language of kindness.", "author": "William Arthur Ward", "category": "kindness", "emotion": "positive"}
]

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