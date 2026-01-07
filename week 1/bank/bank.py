user_prompt= input("Greetings: ").lower().strip().split()

if user_prompt[0].startswith("hello"):
    print("$0")
    
elif user_prompt[0].startswith("h"):
    print("$20")
else :
    print("$100")