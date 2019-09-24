def Test1():
    file=open('knn.py','r',True)
    for line in file:
        print(line)

def Test2():
    file=open('knn.py','r',True)
    lines=file.readlines()
    for line in lines:
        print(line)


def Test3():
    file=open('knn.py','r',True)
    while True:
        line=file.readline()
        if not line:
            break
        print(line)

if __name__=='__main__':
    Test3()