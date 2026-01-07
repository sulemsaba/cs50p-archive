def main():
    #To Get user input first
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False
    chek_no = False  

    for char in s:

        if char.isdigit():
            if not chek_no:
                if char == '0':
                    return False
                chek_no = True
        elif chek_no:
            return False
    return True

if __name__ == "__main__":
    main()