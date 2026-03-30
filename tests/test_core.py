import sys
import os
#add the root directory to the path to allow importing quote_pkg
sys.path.insert(0, os.path.abspath("."))

import pytest
from quote_pkg import core


#QuoteByCategory tests

#make sure the function returns a string
def test_returns_string():
    result = core.QuoteByCategory("motivational")
    assert isinstance(result, str)
#make sure the function's output is not empty
def test_output_not_empty():
    result = core.QuoteByCategory("motivational")
    assert len(result) > 0
#make sure the takes in categories regardless of case
def test_case_insensitive_category():
    result1 = core.QuoteByCategory("motivational")
    result2 = core.QuoteByCategory("MOTIVATIONAL")
    assert isinstance(result1, str)
    assert isinstance(result2, str)

# QuoteByEmotion tests

def test_quote_by_emotion_scenarios_return_string():
    for emotion in ["sad", "happy", "madness", "fear"]:
        result = core.QuoteByEmotion(emotion)
        assert isinstance(result, str)
        assert len(result) > 0

def test_quote_by_emotion_invalid_emotion_raises():
    with pytest.raises(ValueError, match="Emotion not found"):
        core.QuoteByEmotion("unknown_emotion")

# QuoteRandom tests

# test random deterministically is a bit harder,
# here the monkeypatch from pytest is used

def test_quote_random_return_string_from_dataset(monkeypatch):
    test_data = [{"text": "foo"}, {"text": "bar"}]
    monkeypatch.setattr(core, "quotes", test_data)
    monkeypatch.setattr(core.random, "choice", lambda seq: seq[1])

    result = core.QuoteRandom()
    assert isinstance(result, str)
    assert result == "bar"

def test_quote_random_empty_quote_raises_value_error(monkeypatch):
    monkeypatch.setattr(core, "quotes", [])
    with pytest.raises(ValueError, match="quote list is empty"):
        core.QuoteRandom()

def test_quote_random_none_text_raise_value_error(monkeypatch):
    monkeypatch.setattr(core, "quotes", [{"text": None}])
    monkeypatch.setattr(core.random, "choice", lambda seq: seq[0])
    with pytest.raises(ValueError, match="invalid quote object"):
        core.QuoteRandom()

def test_quote_random_non_string_text_raise_value_error(monkeypatch):
    monkeypatch.setattr(core, "quotes", [{"text": 123}])
    monkeypatch.setattr(core.random, "choice", lambda seq: seq[0])
    with pytest.raises(ValueError, match="invalid quote text"):
        core.QuoteRandom()