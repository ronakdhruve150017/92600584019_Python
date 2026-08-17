print("===Data Type===")

a   = 10          # Integer
b   = 5.5         # Float
c   = "Hello"     # String
num = 3+4j        # Complex
d   = True        # Boolean
l   = [1,2,3]     # List
t   = (4,5,6)     # tuple
dic = {"name":"Ronak","age":19}  #Dictionary
s   = {7,8,9}     # Set


print("a=",a,"type=",type(a))
print("b=",b,"type=",type(b))
print("c=",c,"type=",type(c))
print("comp=",num,"type=",type(num))
print("d=",d,"type=",type(d))
print("list=",l,"type=",type(l))
print("tuple=",t,"type=",type(t))
print("dictionary=",dic,"type=",type(dic))
print("set=",s,"type=",type(s))


print("===Type Casting===")


x = float(a)            # int to float
y = int(b)              # float to int
z = str(a)              # int to string
list_to_tuple=tuple(l)  #List to Tuple

print("Int to Float:", x)
print("Float to Int:", y)
print("Int to String:", z)
print("List to tuple:",list_to_tuple)
