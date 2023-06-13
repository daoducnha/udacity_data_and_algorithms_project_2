This is implement of LRU cache

The DoubleNode class represents a node in the doubly linked list. It has a key and a value, as well as next and previous pointers to the next and previous nodes in the list.
The DoubleLinkedList class represents the doubly linked list structure
The LRU_Cache class represents the LRU Cache it has capacity 5 element 
    The get method: retrieves an item from the cache based on its key. Big0 is O(1) because accessing a value in a dictionary and moving a node in a doubly linked list both take constant time.
        If the item is found, it moves the corresponding node to the head of the doubly linked list and returns its value. 
        If the item is not found, it returns -1.
    The set method: adds a new item to the cache. Big0 is O(1) because adding a value to a dictionary, creating a new node, and adding the node to the head of a doubly linked list all take constant time.
        If the cache is already at capacity, it deletes the least recently used item (which is the tail of the doubly linked list) and removes its corresponding entry from the hash_data dictionary. It then adds the new item to the head of the doubly linked list and adds a new entry to the hash_data dictionary.