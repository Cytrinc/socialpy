# cytrinc 0.0.2
# this is tested in vscode

line = "------------------------------------------------------------"

print(line)
print("welcome to cytrinc")

while True:
 com = input("type a command: ")

 if com == "login":
   print("Logging in accounts is currently not available!")
 elif com == "signin":
    print("Account making is currently not available!")
 elif com == "help":
    print(line)
    print("'signin' - Make an account")
    print("'login' - login into an account")
 else:
    print("'" + com + "' is not a valid command")
