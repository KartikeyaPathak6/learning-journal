def main():
    x=input("File name: ").strip().lower()
    ext(x)
    return 0

def ext(e):
    match e:
        
        case e.endswith(".gif"):
            print("image/gif")
        case e.endswith(".jpg"):
            print("image/jpg")
        case e.endswith(".jpeg"):
            print("image/jpeg")
        case e.endswith(".png"):
            print("image/png")
        case e.endswith(".pdf"):
            print("file/pdf")
        case e.endswith(".txt"):
            print("file/text")
        case e.endswith(".zip"):
            print("file/zip")
    return e

main()