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
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)
    
#Test if is within a range
def test_between(n, x, y):
    assert n >= x and n <= y, "{0} is greater than {2} or less than {1}".format(n, x, y)
    
def test_exception_was_raised(func, args, message):
    """
    This test takes a function, arguments and a message as arguments. It can be
    used to test if the exception is raised and the correct message is thrown.
    """
    try:
        func(*args)
        assert False, "Exception was not raised."
    except Exception as e:
        assert e.args[0] == message, "The message that was provided did not match the message thrown."
