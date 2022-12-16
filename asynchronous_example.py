from time import sleep



def count():
    for i in range(10):
        print(i)
        sleep(0.2)


def run():
    for _ in range(5):
        count()



if __name__ == '__main__':
    run()