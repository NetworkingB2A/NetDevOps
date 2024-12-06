def is_greater(a, b):
    # returns True if 'a' is greater
    if a < b:
        return False
    return True


if __name__ == "__main__":
    # output is 'True'
    print(is_greater(5, 5))
    # TypeError
    print(is_greater(5, "four"))