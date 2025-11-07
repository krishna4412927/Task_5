
def run(data):
    result = ""
    for c in data:
        if c.isalpha():
            shift = 1
            if c.islower():
                result += chr((ord(c) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(c) - 65 + shift) % 26 + 65)
        else:
            result += c
    return result
