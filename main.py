import string

def extract_birds(message:str):
    if type(message) != str:
        raise TypeError("Message must be str")
    for char in (message):
        if char in string.punctuation:
            message = message.replace(char, " ")
    return message.split()

print(extract_birds("Качка, Гуска; Курка. Півень: Індик"))