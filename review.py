# Review 1

def add_to_list(value, my_list= []):  # Err: my_list = [] will generate a list at first usage,
    # so multiple call will only generate one list
    my_list.append(value)
    return my_list


# Solution:
def add_to_listFix(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# # Err check:
# list1 = add_to_list(1)
# list2 = add_to_list(2)
# print(list1)
# print(list2)
# assert list1 == list2
# # Fix Check:
# list3 = add_to_listFix(1)
# list4 = add_to_listFix(2)
# print(list3)
# print(list4)
# assert list3 != list4

# Review 2

def format_greeting(name, age):  # Err: name and age will not be involved in the return string.
    return "Hello, my name is {name} and I am {age} years old."


# Solution:
def format_greetingFix(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# # Err check:
# print(format_greeting("Anthony Davis", 30))
# # Fix Check:
# print(format_greetingFix("Anthony Davis", 30))


# Review 3

class Counter:
    def __init__(self):
        self.count += 1  # Err: count is used before initialized, err will show in Counter's initial.
        # Also count should be private

    def get_count(self):
        return self.count


# Solution:
class CounterFix:
    def __init__(self):
        self.__count = 0

    def get_count(self):
        self.__count += 1
        return self.__count


# # Err check:
# cnt = Counter()
# # Fix Check:
# cntFix = CounterFix()
# for _ in range(9):
#     cntFix.get_count()
# assert cntFix.get_count() == 10

# Review 4


import threading


class SafeCounter:  # Err: SafeCounter not safe, need to add lock to avoid concurrent error
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class SafeCounterFix:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock

    def increment(self):
        with self.lock:
            self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

for t in threads:
    t.join()


# Review 5

def count_occurrences(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item] = + 1  # Err: error usage,

        else:

            counts[item] = 1

    return counts


def count_occurrencesFix(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item] += 1

        else:

            counts[item] = 1

    return counts


# Err Check:
testList = [1, 2, 2, 3, 4]
print(count_occurrences(testList))
# Fix Check:
testFixList = [1, 2, 2, 3, 4]
print(count_occurrencesFix(testFixList))
