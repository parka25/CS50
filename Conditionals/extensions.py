input = input("File: ")
input2 = input.lower()

if ".gif" in input2:
    print("image/gif")
elif ".jpg" in input2:
    print("image/jpg")
elif ".jpeg" in input2:
    print("image/jpeg")
elif ".png" in input2:
    print("image/png")
elif ".pdf" in input2:
    print("application/pdf")
elif ".txt" in input2:
    print("text/plain")
elif ".zip" in input2:
    print("application/zip")
else:
    print("application/octet-stream")