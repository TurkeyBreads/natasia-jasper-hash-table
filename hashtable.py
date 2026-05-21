

def _hash_key(key: str, p: int = 53) -> int:
    """Hashes the key using the rolling polynomial algorithm.

    Arguments:
    - key: str
      The key to be hashed.
    - p: int
      A prime number used for the rolling polynomial algorithm

    Returns:
    - the hashed location (int)
    """
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * p**i
    return total


class HashTable:
    """A hashtable without collision resolution.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with

    Attributes:
    - size: int
      The number of slots that the hash table has
    - length: int
      The number of records contained in the hash table
    """

    def __init__(self, size: int):
        self.size = size
        self.length = 0
        self._data = [None] * size

    def __repr__(self) -> str:
        return f"HashTable(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        self._data[_hash_key(key) % self.size] = value
        self.length += 1

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        datum = self._data[_hash_key(key) % self.size]
        
        if datum is None:
            raise KeyError(f"Key '{key}' does not exist")
        return datum

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size

        if self._data[index] is None:
            raise KeyError(f"Key '{key}' does not exist")
        self._data[index] = None
        self.length -= 1

class HashTableLinearProbing(HashTable):
    """A hashtable that implements collision resolution using
    linear probing.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        self.length = 0
        self._data = [(None, None)] * self.size

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        if self.length == self.size:
            raise RuntimeError("Hash Table is full")

        index = _hash_key(key) % self.size
        datum = self._data[index]
   
        if datum[0] is not None and datum[0] != key:
            index += 1
            while True:
                try:
                    index += 1
                except IndexError:
                    index = 0
                
                if self._data[index][0] is None:
                    break
            
        self._data[index] = (key, value)
        self.length += 1

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size
        datum = self._data[index]

        if datum[0] is None:
            raise KeyError(f"Key '{key}' does not exist")
        
        if datum[0] == key:
            return datum[1]
        
        index += 1
        while self._data[index][0] is not None:
            index += 1
            while True:
                try:
                    index += 1
                except IndexError:
                    index = 0
                
                if self._data[index][0] is None:
                    break
        
        return self._data[index][1]

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        if self.length == 0:
            raise RuntimeError("Hash Table is empty")

        index = _hash_key(key) % self.size
        datum = self._data[index]

        if datum[0] is None:
            raise KeyError(f"Key '{key}' does not exist")
        
        if datum[0] == key:
            self._data[index] = (None, None)

        index += 1
        while self._data[index][0] is not None:
            index += 1
            while True:
                try:
                    index += 1
                except IndexError:
                    index = 0
                
                if self._data[index][0] is None:
                    break
        
        self._data[index] = (None, None)
        self.length -= 1


class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        raise NotImplementedError

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError


if __name__ == "__main__":
    import csv

    ht1 = HashTable(15)

    with open("student-data.csv", "r", newline='') as f:
        reader = csv.DictReader(f)

        for record in reader:
            ht1.setitem(record["id"], record)

    ht2 = HashTableLinearProbing(15)

    with open("student-data.csv", "r", newline='') as f:
        reader = csv.DictReader(f)

        for record in reader:
            ht2.setitem(record["id"], record)
