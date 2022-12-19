def main():
    faces = input("type anything you want: ")
    text = convert_face(faces)
    print(text)

def convert_face(faces):
    faces1 = faces.replace(":)", "😀")
    faces2 = faces1.replace(":(", "🙁")
    return faces2

main()