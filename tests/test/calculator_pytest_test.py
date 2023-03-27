import pytest
from tests.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4

def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert 'Выражение должно содержать хотя бы один знак (+-*/)' == error.value.args[0]

if __name__ == '__main__':
    pytest.main()