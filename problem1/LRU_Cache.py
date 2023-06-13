class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.previous = node
        self.head = node

    def update_node(self, node):
        pass

    def move_head(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.previous
            node.previous.next = self.tail

            self.head.previous = node
            node.next = self.head
            self.head = node
            return

        node.previous.next = node.next
        node.next.previous = node.previous

        self.head.previous = node
        node.next = self.head
        self.head = node


    def delete_tail(self):
        self.tail = self.tail.previous
        self.tail.next = self.tail


class LRU_Cache(object):

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.hash_data = dict()
        self.double_linked_list_data = DoubleLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        if self.hash_data.get(key):
            node = self.hash_data.get(key)
            self.double_linked_list_data.move_head(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if len(self.hash_data) == self.capacity:
            # delete tail
            tail = self.double_linked_list_data.tail
            del self.hash_data[tail.key]
            self.double_linked_list_data.delete_tail()

        node = DoubleNode(key, value)
        self.double_linked_list_data.append_head(node)
        self.hash_data[key] = node


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)

our_cache.set(6, 6)


print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Empty Cache
our_cache = LRU_Cache(0)
print(our_cache.get(1))       # returns -1 because the cache is empty

# Test Case 2: Large Cache
our_cache = LRU_Cache(1000000)
for i in range(1000000):
    our_cache.set(i, i)
print(our_cache.get(999999))  # returns 999999

# Test Case 3: Repeated Keys
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(1, 10)
our_cache.set(2, 20)
our_cache.set(3, 30)
print(our_cache.get(1))       # returns 10
print(our_cache.get(2))       # returns 20
print(our_cache.get(3))       # returns 30