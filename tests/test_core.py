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