def new_decoration(func):

    def wrap_func():
        print("CODE HEE BEFORE EXECUTING FUNC")

        func()

        print("FUNC() HAS BEEN CALLED")

    return wrap_func


@new_decoration
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

# func_needs_decorator = new_decoration(func_needs_decorator)
func_needs_decorator()
