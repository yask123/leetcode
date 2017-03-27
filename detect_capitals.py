'''
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
'''


def detect_capital(s):

    if char_capital(s[0]) or all_char_capital(s) or all_char_lowercase(s):
        return True
    return False


def char_capital(s):
    if ord(s[0]) >= ord('A') and ord(s[0]) <= ord('Z'):
        return True
    return False


def all_char_capital(s):

    for each_char in s:
        if char_capital(each_char) == False:
            return False
    return True


def all_char_lowercase(s):
    for each_char in s:
        if char_capital(each_char):
            return False
    return True

print detect_capital('leethode')