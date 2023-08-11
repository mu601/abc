from unittest.mock import patch
from src.functions import print_list

@patch('builtins.print')
def test_print_list(mock_print):
    # arrange 
    test_data =  ['water', 'coke', 'pepsi']

    # act 
    print_list(test_data)

    # assert
    assert mock_print.call.count(len(test_data))
    mock_print.assert_any_call(0, 'water')
    mock_print.assert_any_call(1, 'coke')    
    mock_print.assert_any_call(2, 'pepsi')