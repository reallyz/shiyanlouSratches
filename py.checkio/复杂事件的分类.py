def between_markers(text: str, begin: str, end: str) -> str:
    e = text.find(end)
    s = text.find(begin)
    if e+s==-2:
        return text
    if s==-1:
        return text[:e]
    if e==-1:
        return text[s+len(begin):]
    if e-s<0:
        return ''
    else:
        return text[s+len(begin):e]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('No[/b] hi', '[b]', '[/b]'))


    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
