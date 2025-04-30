"""
Topic: Mixins and Method Resolution Order (MRO)
This example demonstrates mixins and method resolution order (mro) in Python with clear comments.

Mixins should not stand alone — they are meant to be combined with other classes.

Mixins add utility methods (like log()).

They don’t define full behavior, just extend it.

"""
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Worker:
    def work(self):
        print("Working...")

class Manager(LoggerMixin, Worker):
    def manage(self):
        self.log("Manager managing workers.")

m = Manager()
m.work()
m.manage()

'''




# MRO Example
class A:
    def process(self):
        print("Process in A")

class B(A):
    def process(self):
        print("Process in B")

class C(A):
    def process(self):
        print("Process in C")

class D(B, C):
    pass

d = D()
d.process()
print(D.mro())
'''