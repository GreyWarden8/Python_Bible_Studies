import queue

q = queue.PriorityQueue()

q.put((8,"Some String"))
q.put((1,2023))
q.put((90,True))
q.put((2,10.23))

while not q.empty():
    print(q.get()[1])

    
