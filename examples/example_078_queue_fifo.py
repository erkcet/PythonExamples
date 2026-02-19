from queue import Queue

q = Queue()
for item in ["a", "b", "c"]:
    q.put(item)
while not q.empty():
    print(q.get())
