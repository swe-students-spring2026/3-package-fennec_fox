import quote_pkg as quote

#our package ^

def main():
    # QuoteByCategory quick examples
    print("=" * 40)
    print("QuoteByCategory")
    print("Available categories: motivational, historical, funny, reflective, and kindness.")
    print("=" * 40)

    category_1 = quote.QuoteByCategory("motivational")
    print("motivational sample:", category_1)
    category_2 = quote.QuoteByCategory("historical")
    print("historical sample:", category_2)
    category_3 = quote.QuoteByCategory("funny")
    print("funny sample:", category_3)
    category_4 = quote.QuoteByCategory("reflective")
    print("reflective sample:", category_4)
    category_5 = quote.QuoteByCategory("kindness")
    print("kindness sample:", category_5)
    print("\n")

    # QuoteByAuthor quick examples
    print("=" * 40)
    print("QuoteByAuthor")
    print("Author lookup is case insensitive.")
    print("=" * 40)

    author_1 = quote.QuoteByAuthor("roosevelt")
    print("roosevelt sample:", author_1)
    author_2 = quote.QuoteByAuthor("Aristotle")
    print("Aristotle sample:", author_2)
    try:
        author_3 = quote.QuoteByAuthor("unknown author")
        print("unknown author sample:", author_3)
    except ValueError as error:
        print("unknown author sample:", error)
    print("\n")

    # QuoteRandom examples
    print("=" * 40)
    print("QuoteRandom")
    print("Returns a random quote from the full dataset.")
    print("=" * 40)

    random_1 = quote.QuoteRandom()
    print("random example 1:", random_1)
    random_2 = quote.QuoteRandom()
    print("random example 2:", random_2)
    random_3 = quote.QuoteRandom()
    print("random example 3:", random_3)
    print("\n")

    # QuoteByEmotion examples
    print("=" * 40)
    print("QuoteByEmotion")
    print("Supports scenario words and direct emotion labels.")
    print("Scenario inputs: sad, happy, madness, fear.")
    print("Direct emotion inputs: inspired, hopeful, determined, " \
    "focused, thoughtful, resilient, confident, serious, playful, " \
    "sarcastic, light, witty, contemplative, calm, healing, warm, " \
    "compassionate, kind, positive.")
    print("=" * 40)

    print("\nScenario-based emotion inputs:")
    emotion_1 = quote.QuoteByEmotion("sad")
    print("sad example:", emotion_1)
    emotion_2 = quote.QuoteByEmotion("happy")
    print("happy example:", emotion_2)
    emotion_3 = quote.QuoteByEmotion("madness")
    print("madness example:", emotion_3)
    emotion_4 = quote.QuoteByEmotion("fear")
    print("fear example:", emotion_4)

    print("\nDirect emotion lookup:")
    direct_1 = quote.QuoteByEmotion("positive")
    print("positive example:", direct_1)
    direct_2 = quote.QuoteByEmotion("playful")
    print("playful example:", direct_2)
    direct_3 = quote.QuoteByEmotion("thoughtful")
    print("thoughtful example:", direct_3)
    direct_4 = quote.QuoteByEmotion("resilient")
    print("resilient example:", direct_4)

    print("\nInvalid emotion example:")
    try:
        quote.QuoteByEmotion("unknown_emotion")
    except ValueError as error:
        print("unknown_emotion example:", error)

    print("You have now seen examples for all exported package functions.")


if __name__ == "__main__":
    # This block ensures the tutorial runs only when executing this file directly.
    main()
