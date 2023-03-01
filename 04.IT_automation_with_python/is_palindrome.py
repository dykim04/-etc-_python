def is_palindrome(str):
    str = str.lower().replace(" ", "")
    _str = str[::-1]
    _str = _str.lower().replace(" ", "")
    # print(str)
    # print(_str)
    if (str == _str):
        return (True)
    else:
        return (False)

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True