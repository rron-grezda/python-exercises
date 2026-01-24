def say_hello():
    print("Hello Rron!")

say_hello()

print("---------------------")

db_username = "Rron Grezda"
db_password = "1234"

def login():
    username = input("Shkruaj username-in tend: ")
    password = input("Shkruaj password: ")

    if username == db_username and password == db_password:
            print("Home page")
    else:
        print("Wrong username or password!")

login()

print("---------------------")

def pershendtje(username):
    return "Hello " + username

username = input("Shkruaj username tend: ")
print(pershendtje(username))


print("---------------------")

def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome on board!")

greet("Rron", "Grezda")
greet("Albina", "Grezda")

print("---------------------")

def get_name(name):
    print("Hello", name)

get_name("Rron")

print("---------------------")

def even_or_odd(number):
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

num = int(input("Enter a number: "))
even_or_odd(num)
















