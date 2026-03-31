# fennec-fox-quotes

[Badges]

Fennec-fox-quotes is a python package that selects random quotes from a database by category, author or emotion.

## Installation

[Our Pypl](https://pypi.org/project/fennec-fox-quotes/0.1.0/)

Install ```fennec-fox-quotes``` with pip:
```
pip install fennec-fox-quotes
```

## Usage
[Example program]()

You can import the package to a program using:

```python
import fennec-fox-quotes
```

## Documentation

```QuoteByCategory(category)``` chooses a random quote of a certain category. The possible categories are: motivational, historical, funny, reflective and kindness.

```python
import fennec-fox-quotes as quote

print(quote.QuoteByCategory('motivational'))
# An example output would be:
# The best way to get started is to quit talking and begin doing.
```

```QuoteByAuthor(author)``` chooses a random quote of a certain author. The search is partially-matched and case insensitive.

```python
import fennec-fox-quotes as quote

print(quote.QuoteByAuthor('roosevelt'))
# An example output would be:
# Believe you can and you're halfway there.
```

```QuoteRandom()``` gives a completely random quote from the database.
```python
import fennec-fox-quotes as quote

print(quote.QuoteRandom())
# Outputs a random quote
```

```QuoteByEmotion(emotion)``` returns a random quote that matches the given emotion state. A built-in emotion, in the chart provided below, will be resolved into multiple sub-emotions in the search. If the input value is not a built-in emotion, the function will attempt to search for the emotion directly in the database.

| Input  |  Sub-emotions |
|---|---|
| sad |  healing, thoughtful, contemplative, serious |
|  happy | playful, light, witty, positive, warm, calm, kind, compassionate  |
|  madness |  sarcastic, witty, playful, determined, focused |
| fear | confident, resilient, hopeful, determined |

```python
import fennec-fox-quotes as quote

print(quote.QuoteByEmotion('sad'))
# Output a random quote of one of the following categories: healing, thoughtful, contemplative, serious

print(quote.QuoteByEmotion('positive'))
# Output a random quote of the "positive" emotion category
```

## Environment, Building and Testing

### Prerequisites
- Python 3.14
- pipenv

1. Clone the repository:
```bash
git clone https://github.com/swe-students-spring2026/3-package-fennec_fox.git
cd 3-package-fennec_fox
```

2. Install dependencies and activate virtual environment:
```bash
pipenv install --dev
pipenv shell
```

3. Building and Testing:
To test the code, use:
```bash
pytest
```

To build package artifacts, use:
```bash
python -m build
```

## Enviornment variables and data

This package does not require and environment variables to run. To modify the database, modifiy [data.py](/quote_pkg/data.py).

## Teammates
[](https://github.com/tx715)

[Han Xiao](https://github.com/vick12333)

[Sheldon Xie](https://github.com/FilthyS)

[Tim Xu](https://github.com/TimXu2006)

[](https://github.com/jbx202)