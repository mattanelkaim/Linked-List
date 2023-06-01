from typing import Union, Any, Iterable


class ListNode:
    def __init__(self, data: Any):
        self._data, self._next = data, None

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, new_data: Any) -> None:
        self._data = new_data

    @property
    def next(self) -> Union["ListNode", None]:
        return self._next

    @next.setter
    def next(self, new_next: Union["ListNode", None]) -> None:
        self._next = new_next

    def __str__(self) -> str:
        return f"(data={self._data}, next={self._next})"


class MyList:
    def __init__(self):
        # Initializes an empty list
        self.head = self.tail = None

    def append(self, data: Any) -> None:
        """
        Creates a new ListNode object and adds it to the list
        :param data: New data to append
        :return: None
        """
        node = ListNode(data)
        if not self.length():  # length 0
            self.head = self.tail = node
        else:
            self.tail.next = self.tail = node

    def extend(self, other: Iterable) -> None:
        """
        Appends all elements from another iterable (any)
        :param other: Iterable to append
        :return: None
        """
        if not isinstance(other, Iterable):
            raise TypeError(f"{other} is not iterable")
        [self.append(item) for item in other]

    def length(self) -> int:
        """
        Gets the num of nodes in list
        :return: length of this list
        """
        # Handle edge-case
        if self.head is None:
            return 0

        current_node, length = self.head, 1
        while current_node.next is not None:
            length += 1
            current_node = current_node.next
        return length

    def pop(self, target: int = 0) -> Any:
        """
        Removes a node with a given index from current list
        :param target: Index to remove
        :return: Value of popped element
        """
        if self.head is None:
            raise IndexError("List is empty")
        if not isinstance(target, int):
            raise ValueError("Index must be an integer")
        length = self.length()
        if target >= length or target < -length:
            raise IndexError("Given index is not in list")

        # Handle edge-case
        if target == 0:
            popped_value = self.head.data
            self.head = self.head.next
            return popped_value

        current_node = self.head
        if target > 0:  # Popping a positive index
            # Reach node to remove
            for _ in range(target - 1):
                current_node = current_node.next
            popped_value = current_node.next.data
            current_node.next = current_node.next.next

            # Edge-case of removing last node
            if current_node.next is None:
                self.tail = current_node  # Update last node

            return popped_value
        else:  # Popping a negative index
            if -target != length:
                # Reach node to remove
                for _ in range(length - 1 + target):
                    current_node = current_node.next
                popped_value = current_node.next.data
                current_node.next = current_node.next.next

                # Edge-case of removing last node
                if current_node.next is None:
                    self.tail = current_node  # Update last node

                return popped_value
            else:
                # Pop first node
                popped_value = self.head.data
                self.head = self.head.next

                # Edge-case of removing last node
                if self.head is None:
                    self.tail = self.head  # Update last node

                return popped_value

    def count(self, to_search: Any) -> int:
        """
        Counts occurrences of value in list
        :param to_search: Value to count
        :return: # of occurrences
        """
        times_found = 0  # Counter
        current_node = self.head

        while current_node is not None:
            if current_node.data == to_search:
                times_found += 1
            current_node = current_node.next

        return times_found

    def index(self, to_search: Any) -> int:
        """
        Finds the first index of the node with given value
        :param to_search: The value to search
        :return: Index of first occurrence
        """
        index = 0
        current_node = self.head

        while current_node is not None:
            if current_node.data == to_search:
                return index
            index += 1
            current_node = current_node.next

        raise ValueError(f"{repr(to_search)} is not in list")

    def insert(self, index: int, value: Any) -> None:
        """
        Appends the value in a specified index in list TODO
        :param index: Index to append value
        :param value: The value to append
        :return: None
        """
        raise NotImplementedError("Not implemented yet")

    def remove(self, to_remove: Any) -> None:
        """
        Removes the first occurrence of value from list
        :param to_remove: Value to remove
        :return: None
        """
        self.pop(self.index(to_remove))

    def clear(self) -> None:
        """
        Removes all nodes from a list
        :return: None
        """
        self.head = self.tail = None

    def reverse(self):
        reverse_linked_list(self.head)
        self.head, self.tail = self.tail, self.head
        return self


def reverse_linked_list(head: "ListNode") -> Union["ListNode", None]:
    """
    Reverses the nodes in the list object, recursively
    :param: Head of list to reverse
    :return: Reversed list
    """
    if head is None or head.next is None:
        return head

    reversed_list = reverse_linked_list(head.next)

    head.next.next = head
    head.next = None

    return reversed_list


first_list = MyList()
first_list.append(1)
first_list.append("hi")
first_list.append(3.14)
print(f"First Node = {first_list.head}")
print(f"Last Node = {first_list.tail}")
first_list.reverse()
print(f"First Node = {first_list.head}")
print(f"Last Node = {first_list.tail}")
print(f"{first_list.length() = }")
