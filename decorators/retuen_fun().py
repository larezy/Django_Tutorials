def hello (name = 'lael'):
    print("Hey Mr. {}, this is the first statement inside the hello()".format(name))

    def greet():
        print("This is inside the greet()")

    def excerise():
        print("This is inside the excerise()")

    if name == 'lael':
        return greet
    else:
        return excerise


holder = hello()
holder()