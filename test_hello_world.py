# test hello_world.py
import pytest
from hello_world import HelloWorld

@pytest.fixture
def hello_world():
    """
    Fixture to create an instance of the HelloWorld class.
    """
    yield HelloWorld()
    
def test_get_msg(hello_world) -> None:
    assert hello_world.get_msg() == 'Hello World!'
    
def test_set_msg(hello_world) -> None:
    hello_world.set_msg('set msg')
    assert hello_world.get_msg() == 'set msg'
