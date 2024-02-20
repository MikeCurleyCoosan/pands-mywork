import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print('The queue is {}'.format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print('The current number is {}, and the queue is {}'.format(currentNumber, queue))

print('The queue is now empty')

