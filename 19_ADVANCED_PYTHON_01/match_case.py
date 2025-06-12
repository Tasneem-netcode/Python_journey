value =2 

match value:
    case 1 :
        print("One")
    case 2 :
        print("Two")
    case 3 :
        print("Three")

    case _: #default case 
        print("Invalid")


def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "internal server Error"
        case _:#default case 
            "Unknown status"

print(http_status(200))
print(http_status(404))


# Real-life Example:
command = input("Enter command: ")

match command:
    case "start":
        print("Starting the system...")
    case "stop":
        print("Stopping the system...")
    case "restart":
        print("Restarting...")
    case _:
        print("Unknown command.")



# You can also use guards (conditions) inside case.   
num = 10

match num:
    case x if x > 5:
        print("Greater than 5")
    case _:
        print("5 or less")