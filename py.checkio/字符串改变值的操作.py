def correct_sentence(text: str) -> str:
    l = list(text)
    l[0]=l[0].upper()
    if l[-1]!='.':
        l=l+['.']
    l=''.join(l)
    return l


def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
