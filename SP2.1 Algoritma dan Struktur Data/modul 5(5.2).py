from queue import Queue

q = Queue (maxsize=3)
print(q.qsize()) 

q.put("a")
q.put("b")
q.put("c")

print("\nFull: ", q.full())
print("\nElemen dequeue dari queue")
print(q.get())
print(q.get())
print(q.get())

print("\nKosong: ", q.empty()) 
q.put(1)
print("\nKosong: ", q.empty()) 
print("\nFull: ", q.full())
