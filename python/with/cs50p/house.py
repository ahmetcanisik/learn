name = input("What's your name? ")

match name:
    case "Faruk":
        print("Şanlıurfa")
    case "Ahmet" | "Çağlar" | "Can":
        print("İzmir")
    case "Said" | "Ali":
        print("Adana")
    case "Veysel" | "Yavuz":
        print("Elazığ")
    case _:
        print("Who?")
