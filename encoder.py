def encrypter(data):
    str = []
    for i in data:
        str.append(chr(ord(i)+5))
    s = ''.join(str)
    return s