#Suite of tests

#Test if both are equal
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

#Test if both are not equal
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
#Test if item is in collection
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
#Test if item is not in collection
def test_is_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)