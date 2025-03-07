from binary_search import search  # Assuming binary_search is in binary_search.py

def test_binary_search_found():
    """Test when the target is found in the array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    result = search(arr, target)
    assert result == 4  # The index of 5 is 4

def test_binary_search_not_found():
    """Test when the target is not found in the array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 11
    result = search(arr, target)
    assert result == -1  # 11 is not in the list

def test_binary_search_empty_array():
    """Test with an empty array."""
    arr = []
    target = 5
    result = search(arr, target)
    assert result == -1  # 5 is not in an empty list

def test_binary_search_single_element_found():
    """Test when the array has a single element and the target is found."""
    arr = [10]
    target = 10
    result = search(arr, target)
    assert result == 0  # 10 is at index 0

def test_binary_search_single_element_not_found():
    """Test when the array has a single element and the target is not found."""
    arr = [10]
    target = 5
    result = search(arr, target)
    assert result == -1  # 5 is not in the list

def test_binary_search_large_array():
    """Test with a large array."""
    arr = list(range(1, 10001))  # Array from 1 to 10000
    target = 9999
    result = search(arr, target)
    assert result == 9998  # 9999 is at index 9998

def test_binary_search_first_element():
    """Test when the target is the first element in the array."""
    arr = [1, 2, 3, 4, 5]
    target = 1
    result = search(arr, target)
    assert result == 0  # 1 is at index 0

def test_binary_search_last_element():
    """Test when the target is the last element in the array."""
    arr = [1, 2, 3, 4, 5]
    target = 5
    result = search(arr, target)
    assert result == 4  # 5 is at index 4

def test_binary_search_multiple_elements_same_value():
    """Test with multiple elements with the same value."""
    arr = [1, 2, 2, 2, 3]
    target = 2
    result = search(arr, target)
    assert result == 1  # The first occurrence of 2 is at index 1

