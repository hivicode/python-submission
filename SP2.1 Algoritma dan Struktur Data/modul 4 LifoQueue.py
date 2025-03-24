from queue import LifoQueue

setak = LifoQueue(maxsize=3)

print(setak.qsize())

setak.put("a")
setak.put("b")
setak.put("c")

print("Full : ", setak.full())
print("Size : ", setak.qsize())

print("\nElement dikelaurkan dari stack")
print(setak.get())
print(setak.get())
print(setak.get())

print("\nEmpty: ", setak.empty())