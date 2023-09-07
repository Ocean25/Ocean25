class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    def __str__(self):
        return "My name is iterator"
    def __iter__(self):
        print('iteration\n')
        return self
    def __next__(self):
        print('next\n')
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iter = MyIterator(5)
print(my_iter)
for i in my_iter:
    print(i)