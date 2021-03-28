from multiprocessing import Queue,Lock,Process,shared_memory
def process_data(data,q,lock):
    try:
        lock.acquire()
        shm_1 = shared_memory.SharedMemory(create=True,size=10)
        buffer = shm_1.buf
        for i in range(0,len(data)):

            buffer[i] = pow(data[i],2)
        q.put(buffer)
        shm_1.close()
    except Exception as err:
        raise err
    finally:
        lock.release()
def print_result(q):
    while True:
        data = q.get()
        print(data)
        if data == -1:
            break

def main():
    q = Queue()
    lock = Lock()

    data = [1,2,3,4,5,6,7,8,9,10]

    p1 = Process(target=process_data,args=(data,q,lock))
    p2 = Process(target=print_result,args=(q,))

    p1.start()
    p2.start()

    q.close()
    q.join_thread()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
