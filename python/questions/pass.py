attemepts =3
login = False
RightAns = "passs1234"

while attement > 0:
    passWordd = str(input("Enter the passs word :"))

    if passWordd==RightAns:
        print("login in succesfull")
        login=True
        break
    else:
        print("wrong password")
        attement=attement-1

if not login:
    print("Too many failed attempts. Access denied.")

    

