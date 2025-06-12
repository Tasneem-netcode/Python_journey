n =5 

n : int =5 
# (n.) now i will get all the int functions 

name : str = "Hi"
# name.

#example

def add(x: int, y: int) -> int:
    return x + y

add(2,4)

def add(x, y) :
    return x + y

# add(2,"o")


from typing import List , Tuple , Dict

marks : list[int] = [90,78,89]
coordinates : tuple[float , float] = (12.5, 43.8)
user :dict[str , int] = {"id": 101}
user: Dict[str, int] = {
    "id": 101,
    "age": 21,
    "roll": 45
}



from typing import List , Tuple , Dict , Union

numbers : list[int] = [1,2,3,45,6]

person : Tuple[str , int] = ("Alice" , 30 )

scores : Dict[str , int] = {"alice": 90, "bob" : 80}

# UNION MEANS BOTH STRING AND INT 
identifier : Union[int , str] = "ID123"



