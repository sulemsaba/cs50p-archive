while True:
    try:
        User_input_in_fraction = input("Fraction: ")
        firstNo, secondno = User_input_in_fraction.split("/")

        firstNo = int(firstNo)
        secondno = int(secondno)

        # Reject invalid values
        if firstNo < 0 or secondno <= 0 or firstNo > secondno:
            raise ValueError

        percentage = round((firstNo / secondno) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")

        break

    except (ValueError, ZeroDivisionError):
        pass
