class Simple:
    def __init__(self):
        print("Constructor Called.")

    def __del__(self):
        print("Destructor Called.")


obj = []
for i in range(5):
    obj.append(Simple())
    del obj[0]
    print(i)