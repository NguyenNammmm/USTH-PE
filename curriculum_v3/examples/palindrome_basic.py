def is_palindrome(text):
    if text == "":
        return False

    reversed_text = text[::-1]
    return text == reversed_text
