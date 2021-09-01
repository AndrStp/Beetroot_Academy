# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. 
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. 
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.

# ```
# id_ - is just a random unique integer

# class Boss:
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []

# class Worker:
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss
# ```


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def __repr__(self) -> str:
        return f'Boss: {self.id}, {self.name}, {self.company}'

    @property
    def workers(self):
        return self._workers

    @workers.setter   
    def add_worker(self, *args) -> None:
        workers = list(*args)

        if len(workers) < 1:
            raise ValueError('Cannot be empty')
        else:
            self._workers.extend(workers)
            print(f'The following workers has been added:')
            print(*workers, sep=', ')
                

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss
    
    def __repr__(self) -> str:
        return f'Worker: {self.id}, {self.name}, {self.company}'

    @property
    def boss(self) -> Boss:
        return self.__boss
    
    @boss.setter
    def set_boss(self, boss) -> None:
        if isinstance(boss, Boss):
            self.__boss = boss
        else:
            raise TypeError('Not an instance of Boss class')
    
    @boss.deleter
    def dismiss_boss(self) -> None:
        boss = self.__boss.__name__
        self.__boss = None
        print(boss, 'has been dismissed')


if __name__ == '__main__':
    boss1 = Boss(1, 'Andy', 'A&C')

    w1 = Worker(1, 'Andy', 'A&C', boss1)
    w2 = Worker(2, 'Andy', 'A&C', boss1)

    print(w1.boss)  # -> Boss: 1, Andy, A&C
    print(w2.boss)  # -> Boss: 1, Andy, A&C
    boss1._workers = [w1, w2]
    boss1._workers
    boss1.add_worker = [w1, w2] # -> The following workers has been added: \ Worker: 1, Andy, A&C, Worker: 2, Andy, A&C
    print(boss1.workers) # -> [Worker: 1, Andy, A&C, Worker: 2, Andy, A&C, Worker: 1, Andy, A&C, Worker: 2, Andy, A&C]
    
    try:
        w2.set_boss(w1)
    except TypeError as e:
        print(e) # -> 'Boss' object is not callable
    print()

    boss2 = Boss(2, 'Barbara', 'B&C')

    w3 = Worker(1, 'Anna', 'B&C', boss2)
    w4 = Worker(2, 'Brandy', 'B&C', boss2)

    print(w3.boss)  # -> Boss: 2, Barbara, B&C
    print(w4.boss)  # -> Boss: 2, Barbara, B&C
    boss2._workers = [w3, w4]
    boss2._workers
    boss2.add_worker = [w3, w4] # -> The following workers has been added: \ Worker: 1, Anna, B&C, Worker: 2, Brandy, B&C
    print(boss2.workers) # -> [Worker: 1, Andy, A&C, Worker: 2, Andy, A&C, Worker: 1, Andy, A&C, Worker: 2, Andy, A&C]

