# userB_example_program.py

def format_string(name):
    return f"Hello there, {name}"  # Intentional error: missing exclamation mark

if __name__ == "__main__":
    user_name = "Bob"
    print(format_string(user_name))