def convert()->str:
    """This function take user input and convert imoticoins to emoji automatically"""
    sentence= input()
    sentence=sentence.replace(":)","🙂")
    sentence=sentence.replace(":(","🙁")
    return sentence

def main(parameter) -> str:
    return parameter

print(main(convert()))