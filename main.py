import functools
import operator
import time


def parametrized(delay: int = 0):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print(f'Delay: {delay}')
            before = time.time()
            time.sleep(delay)
            value = function(*args, **kwargs)
            after = time.time()
            print(f'Time: {after - before}')
            return value
        return wrapper
    return decorator


if __name__ == '__main__':
    add = parametrized(delay=1)(operator.add)

    assert add(2, 2) == 4
    assert add.__name__ == operator.add.__name__
    assert add.__doc__ == operator.add.__doc__

    sub = parametrized(delay=1)(operator.sub)

    assert sub(4, 2) == 2
    assert sub.__name__ == operator.sub.__name__
    assert sub.__doc__ == operator.sub.__doc__
