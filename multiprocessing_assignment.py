import multiprocessing
from multiprocessing import Queue,Lock,Process,shared_memory
def process_data(data,array,lock):
    try:
        lock.acquire()
        for id,i in enumerate(data):
            array[id] = pow(i,2)
    finally:
        lock.release()

def main():

    lock = Lock()

    array = multiprocessing.Array('i',10)
    data = [1,2,3,4,5,6,7,8,9,10]

    p1 = Process(target=process_data,args=(data,array,lock))

    p1.start()

    p1.join()

    for id,r in enumerate(data):

        print("Square of num ",r,"is",array[id])

if __name__ == "__main__":
    main()
