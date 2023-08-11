from unittest.mock import Mock, patch
from database.database import get_connection

@patch('database.db.get_connection')
def test_get_connection_working(mock_get_connection):
    
    # Arrange
    mock_get_connection.return_value = True
    expected = True

    # Act
    result = get_connection()

    assert expected == result

@patch('database.db.get_connection')
def test_get_connection_not_working(mock_get_connection):
    
    # Arrange
    mock_get_connection.return_value = False

    # Act
    expected = False
    result = get_connection()

    assert expected == result


# py -m pytest database.py -v
# py -m tests.testing