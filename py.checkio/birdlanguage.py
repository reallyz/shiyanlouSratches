VOWELS = "aeiouy"


def translate(phrase):
    vowels= "aeiouy"
    s=phrase.split()
    d=[]
    for i in s:
        ls=list(i)
        for inx,let in enumerate(ls):
            if let in vowels:
                ls[inx:inx+3]=let
            else:
                ls[inx:inx+2]=let
        afm=''.join(ls)
        d.append(afm)
    return ' '.join(d)

import re
def translatere(phrase):
    phrase = re.sub(r"(?<=[^aeiouy ]{1,1})\w{1,1}","", phrase)
    phrase = re.sub(r"([aeiouy]{1,1})(\1{2,2})", r"\1", phrase)
    return phrase


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
