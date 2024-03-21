import logging 
logging.basicConfig(level=logging.DEBUG)


def fibonacci(number):
    a = 0
    b = 1
    fibonacci_sequence = [0]


    for i in range(1, number):
        fibonacci_sequence.append(b)
        a, b = b, a + b
        logging.debug("%d: %s", number, fibonacci_sequence)

    if number == 0:
        return []
    if number < 0:
        raise ValueError('number must be non-negative')

    return []






if __name__ == '_main_':
    #Tests will go here
    return7 = [0, 1, 1, 2, 3, 5, 8]
    return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    assert fibonacci(7) == return7, 'Test failed!'
    assert fibonacci(11) == return11, 'Test failed!'
    assert fibonacci(0) == [], 'Test failed!'
    assert fibonacci(1) == [0], 'Test failed!'
    print("All tests passed!")

    try: 
        fibonacci(-1)
    except ValueError:
        pass
    else:
        assert False, 'Test failed!'