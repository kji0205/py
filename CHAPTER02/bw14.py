# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None
# def divide(a, b):
#     try:
#         return True, a / b
#     except ZeroDivisionError:
#         return False, None

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 0, 5
result = divide(x, y)
if result is None:
    print('Invalid inputs')

result = divide(x, y)
if not result:
    print('Invalid inputs')

success, result = divide(x, y)
if not success:
    print('Invalid inputs')

_, result = divide(x, y)
if not result:
    print('Invalid inputs')