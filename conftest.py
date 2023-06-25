from stuff.accum import Accumulator
import pytest
import selenium.webdriver

@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()