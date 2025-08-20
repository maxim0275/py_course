from unittest.mock import Mock, patch

from src.external_api import get_summ_rated
from src.utils import get_summ_trans


# проверка передачи корректной валюты
def test_get_summ_rated_success():
    mock_response = Mock()
    mock_response.status_code = 200
    # mock_response.json.return_value = {'result': 500}
    mock_response.json.return_value = lambda: {'result': 0}

    with patch('requests.request', return_value=mock_response):
        result = get_summ_rated("USD", 100)
        assert result == 0


# проверка передачи несуществующей валюты
def test_get_summ_rated_fail():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 0}

    with patch('requests.request', return_value=mock_response):
        result = get_summ_rated("USQ", 100)
        assert result == 0


# проверка передачи пустого словаря
def test_get_summ_trans_empty():
    result = get_summ_trans({})
    assert result == 0
