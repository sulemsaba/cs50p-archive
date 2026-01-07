def greatQuestion()-> str:
    """Ask the user the great question of life and return a response."""
    ask_user= input("What is the answer to the great question of life? >.. ").lower().strip()
    correct= "Yes"
    not_correct= "No"
    if ask_user == "42":
        return correct
    elif ask_user == "forty-two":
        return correct 
    elif ask_user == "forty two":
        return correct
    else:
        return not_correct
    
output= print(greatQuestion())