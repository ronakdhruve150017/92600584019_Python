# Program to demonstrate variable scope

global_var = "I am a global variable"

def outer():
    outer_var = "I am a nonlocal variable"

    def inner():
        nonlocal outer_var
        local_var = "I am a local variable"

        print(local_var)
        print(outer_var)
        print(global_var)

    inner()

outer()
