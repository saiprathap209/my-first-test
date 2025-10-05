# greet_user.py

def greet(name):
    if not name.strip():
        return "Hello, Stranger!"
    return f"Hello, {name}!"

def main():
    print("Welcome to the Greeting App!")
    name = input("Please enter your name: ").strip()
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()

