def myFunc():
    print("Hey , i am the module ")


# myFunc()
if __name__ == "__main__":
    print("We are directly running this code ")

    myFunc()
    print(__name__)