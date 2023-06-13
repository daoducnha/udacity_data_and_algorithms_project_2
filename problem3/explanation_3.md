Node class: Represents a node in a binary tree. 
    It has a value, left and right pointers to its left and right children

Tree class: Represents a binary tree with a root node.
    It has methods to get the root to get root value

HeapElement class: Represents a element in heapq.
    It has a value and frequency of this value in string

function huffman_encoding:  
    function takes a string data as input and returns a tuple containing the encoded string and the Huffman tree
    The function first builds a heap of HeapElement objects then creates a tree from this heap 
    and use function get_encode_values get string after encoding 
    this function has Big0 is O(n log n) because function builds a heap of HeapElement objects, which takes O(n) time then repeatedly pops the two smallest elements from the heap and creates a new tree node, which takes O(log n) time 

function huffman_decoding:
    function takes an encoded string data and a Huffman tree as input and returns the decoded string. The function iterates over each character in the encoded string and traverses the Huffman tree accordingly. If the current node is a leaf node, the function appends its value to the decoding string and resets the current node to the root of the Huffman tree. If the current character is '0', the function sets the current node to its left child, and if the current character is '1',
    this function has Big0 is O(n log n) because the function traverses the Huffman tree for each character in the encoded string, which takes O(log n) time per character.    