B= input() .split()
B_obj =  dict(
    map(
        lambda x : (x[0], int(x[1])) if x[1].isdigit() else (x[0] , x[1]) , 
        zip(B[0::2] , B[1 ::2])
    )
)

print(type(B_obj))
print(B_obj)