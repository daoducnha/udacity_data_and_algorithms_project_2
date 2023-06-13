import sys
import heapq

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root

class HeapElement:
    def __init__(self, value=None, frequency=0):
        self.value = value
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

def huffman_encoding(data):
    heap = []

    char_dict = dict()
    for char in data:
        if char_dict.get(char):
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for key in char_dict:
        heapq.heappush(heap, HeapElement(key, char_dict.get(key)))


    if len(heap) == 1:
        elem = heapq.heappop(heap)
        tree_node = Node(elem.frequency)
        tree_node.left = elem
        tree = Tree(tree_node)
    else:
        while len(heap) > 1:
            first_elem = heapq.heappop(heap)
            second_elem = heapq.heappop(heap)

            if type(first_elem.value) is str and type(second_elem.value) is str:
                tree_node = Node(first_elem.frequency + second_elem.frequency)
                tree_node.left = first_elem
                tree_node.right = second_elem
                sub_tree = Tree(tree_node)
                new_heap_elem = HeapElement(sub_tree, tree_node.value)
                heapq.heappush(heap, new_heap_elem)
            elif type(first_elem.value) is Tree and type(second_elem.value) is not Tree:
                tree_node = Node(first_elem.value.root.value + second_elem.frequency)
                tree_node.left = first_elem.value.root
                tree_node.right = second_elem
                sub_tree = Tree(tree_node)
                new_heap_elem = HeapElement(sub_tree, tree_node.value)
                heapq.heappush(heap, new_heap_elem)
            elif type(first_elem.value) is not Tree and type(second_elem.value) is Tree:
                tree_node = Node(first_elem.frequency + second_elem.value.root.value)
                tree_node.left = first_elem
                tree_node.right = second_elem.value.root
                sub_tree = Tree(tree_node)
                new_heap_elem = HeapElement(sub_tree, tree_node.value)
                heapq.heappush(heap, new_heap_elem)
            else:
                tree_node = Node(first_elem.value.root.value + second_elem.value.root.value)
                tree_node.left = first_elem.value.root
                tree_node.right = second_elem.value.root
                sub_tree = Tree(tree_node)
                new_heap_elem = HeapElement(sub_tree, tree_node.value)
                heapq.heappush(heap, new_heap_elem)

        tree = heapq.heappop(heap).value

    encoded_data = get_encode_values(tree)
    encode_str = ''
    for c in data:
        encode_str += encoded_data.get(c)

    return encode_str, tree

def get_encode_values(tree):
    encoded_dict = dict()
    root = tree.root

    def traverse(node, path):
        if node is None:
            return
        if type(node) is HeapElement:
            encoded_dict[node.value] = ''.join(path)
            return

        left = path + ['0']
        traverse(node.left, left)

        right = path + ['1']
        traverse(node.right, right)

    traverse(root, [])
    return encoded_dict


def huffman_decoding(data,tree):
    decoding_string = ''
    node = tree.root
    for i in data:
        if type(node) is HeapElement:
            decoding_string += node.value
            node = tree.root

        if i == '0':
            node = node.left
        else:
            node = node.right

    if type(node) is HeapElement:
        decoding_string += node.value
    return decoding_string

c
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
print("=============Test case 1=============")
string1 = 'aaaabbc'
encoded_str1, tree = huffman_encoding(string1)
assert huffman_decoding(encoded_str1, tree) == string1

## Test Case 2
print("=============Test case 2=============")
string2 = 'aaaaaaaaaa'
encoded_str2, tree = huffman_encoding(string2)
assert huffman_decoding(encoded_str2, tree) == string2

## Test Case 3
print("=============Test case 3=============")
string3 = 'mississippi'
encoded_str3, tree = huffman_encoding(string3)
assert huffman_decoding(encoded_str3, tree) == string3