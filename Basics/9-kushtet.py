# x=100

# if x > 20:
#     print(str(x) +" eshte me e madhe se 20")
# else:
#     print(str(x)+" eshte me e vogel se 20")


# x = 0

# if x == 0:
#     print(str(x) + " eshte zero")
# elif x>=1 and x<=9:
#     print(str(x) + " eshte numer njeshifrore")
# elif x>=10 and x<=99:
#     print(str(x) + " eshte numer dyshifrore")
# elif x>=100 and x<=999:
#     print(str(x) + " eshte numer treshifrore")
# else:
#     print(str(x) + " eshte me shume se treshifrore")


db_username = "rron.grezda"
db_password = "3698"

username = input("Shkruaj username: ")
password = input("Shkruaj password: ")

if username == db_username:
    if password == db_password:
        print("Home Page")
    else:
        print("Password eshte shtypur gabim!")
else:
    print("Username eshte shtypur gabim!")