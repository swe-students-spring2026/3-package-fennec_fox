import random
from .data import quotes

def QuoteByCategory(category):
    """
    Function for choosing a random quote of a certain category. 
    the possible categories are: motivational, historical, funny, reflective, kindness
    """
    matches =[
        quote["text"]
        for quote in quotes
        if quote["category"].lower() == category.lower()
    ]
    if not matches:
        raise ValueError("Category not found")
    return random.choice(matches)

def QuoteByAuthor(author):
    """
    Function for choosing random quote of a given author.
    The search is partially-match and case insensitive.

    :param author: The author to search for
    :return: A quote of the author if there is at least one match, or -1 if there is none
    """
    author = author.strip().lower()
    matches = [
        quote['text']
        for quote in quotes
        if author in quote.get('author', '').lower()
    ]
    if not matches:
        return -1
    return random.choice(matches)
  
def QuoteRandom() -> str:

    if len(quotes) == 0:
        ValueError("quote list is empty")

    random_obj: object = random.choice(quotes)
    random_quote: str = random_obj["text"];

    if random_quote == None:
        ValueError("invalid quote object")

    if not isinstance(random_quote, str):
        ValueError("invalid quote text")

    return random_quote

def QuoteByEmotion(emotion):
    if not isinstance(emotion, str):
        raise ValueError("Emotion must be a non-empty string")

    normalized_emotion = emotion.strip().lower()
    if not normalized_emotion:
        raise ValueError("Emotion must be a non-empty string")

    emotion_scenarios = {
        "sad": {"healing", "thoughtful", "contemplative", "serious"},
        "happy": {"playful", "light", "witty", "positive", "warm", "calm", "kind", "compassionate"},
        "madness": {"sarcastic", "witty", "playful", "determined", "focused"},
        "fear": {"confident", "resilient", "hopeful", "determined"}
    }

    if normalized_emotion in emotion_scenarios:
        allowed_emotions = emotion_scenarios[normalized_emotion]
    else:
        allowed_emotions = {normalized_emotion}

    matches = []
    for quote in quotes:
        quote_emotion = quote.get("emotion", "").lower()
        if quote_emotion in allowed_emotions:
            matches.append(quote["text"])

    if not matches:
        raise ValueError("Emotion not found")
    
    return random.choice(matches)
