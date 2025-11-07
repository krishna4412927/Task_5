
def run(data):
    vowels = "aeiouAEIOU"
    for v in vowels:
        data = data.replace(v, "*")
    return data
