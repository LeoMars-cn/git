import time

def logTime(func):
    def wrapper(self):
        st = time.time()
        func(self)
        print(f"{self._name} slept for {time.time() - st} seconds.") 
    return wrapper

class Person:
    def __init__(self):
        self._name = ''
        self._age = 0
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

    def introduce(self):
        print(f"My name is {self._name} and I am {self._age} years old.")

    @logTime
    def sleep(self):
        print(f"{self._name} is sleeping for 3 seconds.")
        time.sleep(3)


if __name__ == "__main__":
    p = Person()
    p.name = "John"
    p.age = 30
    p.introduce()
    p.sleep()

