# Hash Table Practice

## Part 0: Hashing function

The following hashing function is provided:

`_hash_key(key)`
- takes in a `string` argument `key`
- returns a hashed `integer` value unique to the key.

The `_hash_key()` function implements the [rolling polynomial algorithm](https://cp-algorithms.com/string/string-hashing.html):  
        
$hash(key) = (\sum_{i=0}^{n-1} key[i].p^i)\ mod\ m$

$ = (key[0] + key[1].p + key[2].p^2 + ... + key[n-1].p^{n-1})\ mod\ m$  
where
- `key` - each key segment is a string. It needs to be converted to its integer ASCII value 
- `p` - a small prime number (if the input is composed of only lowercase letters of the English alphabet,  
  $p = 31$  is a good choice. If the input may contain both uppercase and lowercase letters, then  
  $p = 53$  is a possible choice.)
- `m` - a large prime number (we will use $`10^9+9`$ for this implementation)

**Further learning:** [[ChatGPT] "What hashing functions are commonly used for hash tables?"](https://chatgpt.com/s/t_6a02c3f1f04081919e9ad9096e5c2566)

## Part 1: Hash table without collision resolution

In `hashtable.py`, implement the `HashTable` class:
- `__init__.py` should take a `size` parameter that determines the number of slots that the hashtable is initialised with.
- the fixed-size array that holds key-value pairs is represented as a Python `list`, pre-filled with `None` values
- do not use `list`-mutating methods and operators, such as `list.append()`, `list.extend()`, and list concatenation

and the following methods:
- `setitem(key, value)`
  1. if the hashed location is empty, store the value
  2. if the hashed location is occupied, overwrite the value
- `getitem(key)` - returns the following:
  1. if the hashed location is empty, the key is not found; raise a `KeyError`
  2. if the hashed location is occupied, return the value
- `delitem(key)`
  1. if the hashed location is empty, the key is not found; raise a `KeyError`
  2. if the hashed location is occupied, replace the value with `None`

## Part 2: Use the HashTable to store student data from a CSV file

1. Instantiate a `HashTable` with 15 slots.
2. Extract the records from the `student_data.csv` file into a list of dicts.
3. Add each record into the hash table, with the id (i.e. `"s0011a"`) as the **key**, and the record (i.e. `{"id": "s0011a", "name": "Patrick Tan", "class": "2599"}`) as the **value**
4. Inspect the fixed-size array and the hashtable length: do they tally?

## Part 3: Hash table with collision resolution - linear probing (open addressing / closed hashing)

**Linear probing** is an open-addressing collision resolution technique in hash tables where, upon a collision, the algorithm checks sequential slots (`i + 1`, `i + 2`, ...) linearly until an empty slot is found.

In `hashtable.py`, implement the `HashTableLinearProbing` class with the following methods:
- `setitem(key, value)`
    1. if the hashed location is empty, store the key and value
    2. if the hashed location is occupied and the key matches, store the key and value
    3. if the hashed location is occupied and the key does not match, re-hash the key (using linear probing) and repeat from (1)
- `getitem(key)` - returns the following:
    1. if the hashed location is empty, the key is not found; raise a `KeyError`
    2. If the hashed location is occupied and the key matches, retrieve and return the value
    3. If the hashed location is occupied and the key does not match, re-hash the key (using linear probing) and repeat from (1)
- `delitem(key)`
    1. if the hashed location is empty, the key is not found; raise a `KeyError`
    2. If the hashed location is occupied and the key matches, remove the stored key-value pair. (**Note:** This will break linear probing for subsequent entries; those will need to be re-inserted)
    3. If the hashed location is occupied and the key does not match, re-hash the key (using linear probing) and repeat from (1)

In `main.py`, inspect the fixed-size array and the hashtable length: do they tally now?

**Further learning:** [[ChatGPT] "With open addressing for hash tables, removing key-value pairs can break subsequent probing. What strategies are commonly used to address this?"](https://chatgpt.com/s/t_6a02c7a90e1c8191b4febdfc9a28cbf7)

## Part 4: Hash table with collision resolution - separate chaining (closed addressing / open hashing)

**Separate chaining** is a collision resolution technique in hash tables where multiple elements mapping to the same hash index (bucket) are stored together using an auxiliary data structure, typically a linked list.

In `hashtable.py`, implement the `HashTableSeparateChaining` class:
- Instead of initialising the fixed-size array with `None` values, initialise a linked list in each array cell.
- You may wish to copy your `LinkedList` code from the previous exercise. Note that `Node` will store a `key` and a `value` attribute in addition to `next`.

Implement the following `HashTableSeparateChaining` methods:
- `setitem(key, value)`
    1. Walk the linkedlist at the hashed location.
    2. If the key is found in the linkedlist, update the value at the node where it is found.
    3. If the key is not found in the linkedlist, add a new node with the key-value pair.
- `getitem(key)` - returns the following:
    1. Walk the linkedlist at the hashed location
    2. If the key is found in the linkedlist, retrieve and return the value from the node where it is found.
    3. If the key is not found in the linkedlist, raise a `KeyError`.
- `delitem(key)`
    1. Walk the linkedlist at the hashed location
    2. If the key is found in the linkedlist, unlink the node where it is found.
    3. If the key is not found in the linkedlist, raise a `KeyError`.

In `main.py`, inspect the fixed-size array and the hashtable length: do they tally now?

**Further learning:** [[ChatGPT] "What are some commonly used ways to resolve collisions in a hash table?"](https://chatgpt.com/s/t_6a02c4ba82d881918edede08c4b6bb14)
