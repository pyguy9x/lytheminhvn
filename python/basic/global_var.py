# Ví dụ biến toàn cục
name = "Nguyen Van A"
 
print('truoc:', name)
 
def hello():
    # name = "A handsome"
    print("Hello ", name)
 
hello()
 
print("--name is:", name)

print("-"*30)

name = "Nguyen van A"
 
print("truoc:", name)
 
def hello():
    global name
    name = "B"
    print("Hello ", name)
 
hello()
print("--name is:", name)
# -------Output-----------
# truoc: Nguyen Van A
# Hello  Nguyen Van A
# --name is: Nguyen Van A
# ------------------------------
# truoc: Nguyen van A
# Hello  B
# --name is: B