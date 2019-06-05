def checkio(text: str) -> str:
    import string
    d = dict.fromkeys(string.ascii_lowercase,'')
    print('there!!!')
    print(d)
    text=text.lower()
    print(text)
    for i in text:
        print(i)
        if i.isalpha():
            d[i]=d[i]+i
            print(d[i])
    print(d)


if __name__ == '__main__':
    print("Example:")
    checkio("Hello World!")
    '''
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
    '''