f =open("demo.txt")
content =f.read()
if("twinkle" in content):
    print(" Word Twinkle is present   in this content ")
else:
    print("Not present")
f.close()