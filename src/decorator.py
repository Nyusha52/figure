def exept(func):
    def wrapper(*arg):
        try:
            return func(*arg)
        except AttributeError as a:
            print(f"{a}")

    return wrapper
