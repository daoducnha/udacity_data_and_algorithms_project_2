import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return f"""
            timestamp: {self.timestamp},
            data: {self.data},
            previous_hash: {self.previous_hash},
            hash: {self.hash}
        """


class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        str(self.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        ts = datetime.datetime.now().timestamp()
        if self.head is None:
            current_node = ListNode(Block(ts, data, None))
            self.head = self.tail = current_node
            return
        else:
            pre_block = self.tail.value
            current_block = Block(ts, data, pre_block.hash)
            current_node = ListNode(current_block)

            self.tail.next = current_node
            self.tail = current_node
            return

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

# Test case 1
blockchain = LinkedList()
blockchain.append("First block")
assert blockchain.head.value.hash == blockchain.head.value.calc_hash()

blockchain = LinkedList()
blockchain.append("First Block")
blockchain.append("Second Block")
blockchain.append("Third Block")
blockchain.append("Forth Block")

node = blockchain.head
print(blockchain)

while node and node.next != blockchain.tail:
    assert node.value.hash == node.next.value.previous_hash
    node = node.next