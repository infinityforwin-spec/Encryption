import time
def count(start,end):
    for x in range(start,end):
        print(x)
        time.sleep(2)
    print('end')

count(0,10)