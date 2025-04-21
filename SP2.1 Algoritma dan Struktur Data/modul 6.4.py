from collections import deque 

q = deque() 

q.append('a') 
q.append('b') 
q.append('c') 

print('Initial queue') 
print(q) 

print("\nElement yang dikeluarkan dari queue: ") 
print(q.popleft()) 
print(q.popleft()) 
print(q.popleft()) 

print("Queue setelah element dikeluarkan: ") 
print(q)