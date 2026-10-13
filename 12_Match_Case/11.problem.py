# Problem 11

print(" 1 : pdf : Document  2 : jpg : Image 3 : png : Image 4 : mp3 : Audio 5 : mp4 : Video")
numb = int(input("Enter Extension: "))

match numb:
    case 1:
        print("Document File")
    case 2:
        print("Image File")
    case 3:
        print("Image File")
    case 4:
        print("Audio File")
    case 5:
        print("Video File")
    case _:
        print("Unknown File Type")

