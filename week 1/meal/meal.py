def main():
    #I Ask user for time
    Usertime = input("What time is it? ").strip()
    hours = convert(Usertime)

    # then i Check meal times
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(user_time):
    """Convert time string in 24-hour format to float hours."""
    userInput = user_time.split(":")
    hours = int(userInput[0])
    minutes = int(userInput[1])
    #finaly Convert to float
    return hours + minutes / 60


if __name__ == "__main__":
    main()
