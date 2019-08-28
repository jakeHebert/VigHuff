class Set:
    """
    Python list Implementation of the Set ADP
    """

    def __init__(self):
        """
        Creates an empty Set
        """
        self._items = list()

    def __len__(self):
        """
        Returns the number of items in the list
        """
        return len(self._items)

    def __contains__(self, item):
        """
        Returns True if the set contains the passed in item, else False
        """

    def add(self, item):
        """
        Adds a new item to the set, if the item is not already in the set
        """
        if item not in self._items:
            self._items.append(item)

    def remove(self, item):
        """
        Removes an item from the set if it exists
        """
        if item in self._items:
            self._items.remove(item)

    def __str__(self):
        """
        Returns a string representation of the Set
        """
        return str(self._items)

    def __eq__(self, other_set):
        """
        Returns True if all the items in this set are the same items
        in the passed in other_set, and False otherwise
        """
        if len(self) != len(other_set):
            return False
        else:
            return self.is_subset_of(other_set)

    def is_subset_of(self, other_set):
        """
        Returns True if all the items in this set are also
        in the passed in other_set, and False otherwise
        """
        for item in self:
            if item not in other_set:
                return False
        return True

    def union(self, other_set):
        """
        Creates a new set by combining the items in this set
        with the items of the passed in other_set
        """
        new_set = Set()
        new_set._items = [] + self._items
        for item in other_set:
            if item not in self:
                new_set._items.append(item)
        return new_set

    def intersection(self, other_set):
        """
        Creates a new set consisting of the items that are in both
        this set and in the passed in other_set
        """
        new_set = Set()
        for item in other_set:
            if item in self:
                new_set._items.append(item)
        return new_set

    def difference(self, other_set):
        """
        Creates a new set consisting of the items that are in this set,
        but not in the passed in other_set
        """
        new_set = Set()
        for item in self:
            if item not in other_set:
                new_set._items.append(item)
        return new_set

    def __iter__(self):
        """
        Returns an iterator for traversing this set
        """
        return SetIterator(self._items)


class SetIterator:
    """
    An iterator for the Set ADT implemented as a Python list
    """

    def __init__(self, the_set):
        """
        Initializes the set list, from the one passed in
        Set the current index to 0
        """
        self._set_items = the_set
        self._cur_item = 0

    def __iter__(self):
        """
        Returns this iterator
        """
        return self

    def __next__(self):
        """
        Returns the next item in the set
        """
        if self._cur_item < len(self._set_items):
            item = self._set_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration
