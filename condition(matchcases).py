color=input("Enter a color: ")

match color:
    case "red":
        print("Roses are red.")
    case "blue":
        print("The sky is blue.")
    case "green":
        print("Grass is green.")
    case _:# default case
        print("Color not recognized.")
        