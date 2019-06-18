f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# Put our words in a set for O(1) lookup
word_set = set()
for word in words:
    word_set.add(word.lower())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_neighbors(word):
    pass


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# BFS with path


def find_word_ladder(beginWord, endWord):
    pass


print(find_word_ladder("sail", "boat"))
