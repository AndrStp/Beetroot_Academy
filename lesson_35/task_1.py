"""
Task 1

A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the 
Threading module. Make the class have two global variables, one called counter 
set to 0, and another called rounds set to 100.000. Now implement the run() 
method, let it include a simple for-loop that iterates through rounds 
(e.i. 100.000 times) and for each time increments the value of the counter by 1. 
Create 2 instances of the thread and start them, then join them and check the 
result of the counter, it should be 200.000, right? Run it a couple of times 
and consider some different reasons why you get the answer that you get.
"""

from threading import Thread


class Counter(Thread):
    counter = 0
    rounds = 100_000

    def __init__(self) -> None:
        Thread.__init__(self)
    
    def run(self) -> None:
        for _ in range(Counter.rounds):
            Counter.counter += 1


if __name__ == '__main__':
    counter_1 = Counter()
    counter_1.start()
    count_1 = Counter.counter

    counter_2 = Counter()
    counter_2.start()
    count_2 = Counter.counter

    print(count_1, count_2)

