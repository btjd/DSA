class Hash(object):
    """
    http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
    """
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_func(self, k):
        return k % self.size

    def rehash_func(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, k, v):
        hash_val = self.hash_func(k)

        if self.keys[hash_val] is None:
            self.keys[hash_val] = k
            self.values[hash_val] = v
        else:
            if self.keys[hash_val] == k:
                self.values[hash_val] = v
            else:
                next_loc = self.rehash_func(hash_val)
                while self.keys[next_loc] is not None and self.keys[next_loc] != k:
                    next_loc = self.rehash_func(next_loc)
                if self.keys[next_loc] is None:
                    self.keys[next_loc] = k
                    self.values[next_loc] = v
                else:
                    self.values[next_loc] = v

    def get(self, k):
        # Consider the scenarios where the fisrt hash index gets
        # us to the desired key. If we don't find it then we try
        # with a rehash, if that still fails then the key doesn't
        # exist in our hash table and we return None.
        start_index = self.hash_func(k)
        val = None
        stop = False
        found = False
        current_index = start_index
        while self.keys[current_index] is not None and not found and not stop:
            if self.keys[current_index] == k:
                found = True
                val = self.values[current_index]
            else:
                current_index = self.rehash_func(start_index)
                # This line guarantees that the search will terminate
                #  by checking to make sure that we have not returned 
                # to the initial slot. If that happens, we have exhausted 
                # all possible slots and the item must not be present.
                if current_index == start_index:
                    stop = True
        return val

    def __getitem__(self, k):
        return self.get(k)

    def __setitem__(self, k, v):
        self.put(k, v)
