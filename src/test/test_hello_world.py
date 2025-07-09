import pytest
from tableau_to_lk_package.hello_world import hello_world


def test_hello_world():
    assert hello_world() == "Hello, World!" 