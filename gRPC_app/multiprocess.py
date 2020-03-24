from multiprocessing import Process
import gRPC_clients as client

if __name__ == "__main__":
    count = 5
    processes = {}

    for c in range(count):
        processes[c] = Process(target=client.run)
    
    for c in range(count):
        processes[c].start()
