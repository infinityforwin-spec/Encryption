import time
def enter_name():
    name=input("enter name")
    if name != 'joe':
        print("Dont know you,wait and try again..")
        time.sleep(1)
        print("1")
        time.sleep(2)
        print("2")
        time.sleep(3)
        print("3")
        enter_name()
    else:
        your_name()
def your_name():
    print("Hi Joe")

def client():
    print('hi client')

client()
enter_name()