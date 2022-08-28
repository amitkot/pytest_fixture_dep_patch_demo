import pytest
from unittest import mock
from y import Apple
import sys


@pytest.fixture
def get_apple():
    with mock.patch("y.Banana", spec=True):
        yield Apple()


# @mock.patch("y.Banana", spec=True)
# def test_get_mock_banana(mock_banana):
def test_get_mock_banana(get_apple):
    a = Apple()
    banana = a.get_banana()
    assert banana.result()
