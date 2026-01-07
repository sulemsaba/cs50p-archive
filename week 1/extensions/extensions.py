user_response= input("File name: ").lower().strip()

if user_response.endswith(".gif"):
    print("image/gif")
elif user_response.endswith(".jpg"):
    print("image/jpeg")
elif user_response.endswith(".jpeg"):
    print("image/jpeg")
elif user_response.endswith(".png"):
    print("image/png")
elif user_response.endswith(".pdf"):
    print("application/pdf")
elif user_response.endswith(".txt"):
    print("text/plain")
elif user_response.endswith(".zip"):
    print("application/zip")
else :
    print("application/octet-stream")