from set import Set


class Map:
    """
    Python list Implementation of the Map ADT
    """
    def __init__(self):
        """
        Creates an empty Map
        """
        self._map_entries = []

    def __len__(self):
        """
        Returns the number of items in the set
        """
        return len(self._map_entries)

    def __contains__(self, key):
        """
        Returns True if the map contains the passed in key, else False
        """
        index = self.find_index(key)
        return index is not None

    def add(self, key, value):
        """
        Adds a new entry to the map if the passed in key does not exist.
        Otherwise, the value replaces the current value associated with the key.
        """
        index = self.find_index(key)
        if index is not None:
            self._map_entries[index].value = value
            return False
        else:
            entry = MapEntry(key, value)
            self._map_entries.append(entry)
            return True

    def remove(self, key):
        """
        Removes teh entry associated with the passed in key, when key in map
        """
        index = self.find_index(key)
        if index is not None:
            return self._map_entries.pop(index)
        else:
            print("Key is not in the map")
            return None

    def get_value(self, key):
        """
        Returns teh value associated with teh passed in key, when key in map
        """
        index = self.find_index(key)
        if index is not None:
            return self._map_entries[index].value
        else:
            print("Key is not in the map")
            return None

    def get_entry_set(self):
        """
        Returns a set of the MapEntry objects in the map
        """
        entry_set = Set()
        for entry in self:
            entry_set.add(entry)
        return entry_set

    def get_key_set(self):
        """
        Returns a set of the keys in the map
        """
        key_set = Set()
        for entry in self:
            key_set.add(entry.key)
        return key_set

    def get_value_set(self):
        """
        Returns a set of the values in the map
        """
        value_set = Set()
        for entry in self:
            value_set.add(entry.key)
        return value_set

    def __str__(self):
        """
        Returns a string representation of the map object
        """
        map_str = "{ " + str(self._map_entries[0])
        for i in range(1, len(self)):
            map_str += ", " + str(self._map_entries[i])
        return map_str + " }"

    def __iter__(self):
        """
        Returns an iterator for traversing the keys in the map
        """
        return MapIterator(self._map_entries)

    def find_index(self, key):
        """
        Returns the position of a passed in key, or None if the key is not in the map
        """
        for i in range(len(self)):
            if self._map_entries[i].key == key:
                return i
        return None


class MapEntry:
    """
    The class for holding the key/value pairs of a map
    """
    def __init__(self, key, value):
        """
        Creates a MapEntry with the passed in key/value pair
        """
        self.key = key
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the key/value pair
        """
        return str(self.key) + " : " + str(self.value)


class MapIterator:
    """
    An iterator for the Map ADT implemented as a Python list
    """
    def __init__(self, a_map):
        """
        Initialize the map list, from the one passed in
        Set the current entry to index 0
        """
        self._map_entries = a_map
        self._cur_entry = 0

    def __iter__(self):
        """
        Returns this iterator
        """
        return self

    def __next__(self):
        """
        Returns the next item in the map
        """
        if self._cur_entry < len(self._map_entries):
            item = self._map_entries[self._cur_entry]
            self._cur_entry += 1
            return item
        else:
            raise StopIteration
