from unittest.mock import patch
from src.functions import enter_index, products_list

@patch('builtins.input')
def test_enter_index(mock_input):
     mock_input.return_value = 3
     expected = 3
     result = enter_index(products_list, 'product list' )
     assert result == expected

@patch('builtins.input')
def test_enter_index_multiple_values1(mock_input):
    mock_input.side_effect = ['five', 'one', 'ten', 2]
    expected = 2

    result = enter_index(products_list, 'product_list')
    assert result == expected


    
    #  py -m pytest tests\test_input.py -v
