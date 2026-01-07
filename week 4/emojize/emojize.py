import emoji

def main():
    user_input = input("Input: ")
    emojized = emoji.emojize(user_input, language="alias")
    print("Output:", emojized)

if __name__ == "__main__":
    main()