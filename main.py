import string


def extract_birds(message:str) -> list[str]:
    if not isinstance(message, str):
        raise TypeError("Message must be str")
    for char in message:
        if char in string.punctuation:
            message = message.replace(char, " ")
    return message.split()

if __name__ == "__main__":
    print(extract_birds("Качка, Гуска; Курка. Півень: Індик"))