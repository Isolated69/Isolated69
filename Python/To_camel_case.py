def to_camel_case(string):
    new_str = string.replace('-', '_')
    words = new_str.split('_')
    check = words[0]
    if check[:1].isupper():
        change = False
    else:
        change = True
    camelled = []
    for word in words:
           bword =  word.capitalize()
           camelled.append(bword)
    result = ''.join(camelled)
    if change:
        result = result[:1].lower() + result[1:]
        return result
    else:
        return result


word = 'The-Stealth-Warrior'
to_camel_case(word)

