# Main run file. Holds the User interface
from creater import make_char

def main():
    print("Hello User do you want to create a character?")
    choice = input("enter 1 to create a character 2 to exit")
    if choice == "1":
        make_char()

main()