# TODO remove() the returns..
from typing import Union, Any


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
        self.first_node = self.last_node = None

    def append(self, data: Any) -> None:
        """
        Creates a new ListNode object and adds it to the list
        :param data: New data to append
        :return: None
        """
        node = ListNode(data)
        if not self.length():  # length 0
            self.first_node = self.last_node = node
        else:
            self.last_node.next = self.last_node = node

    def extend(self, other_list: list) -> None:
        """
        Appends all elements from another list (Python built-in)
        :param other_list: list to append
        :return: None
        """
        [self.append(item) for item in other_list]

    def length(self) -> int:
        """
        Gets the num of nodes in list
        :return: length of this list
        """
        # Handle edge-case
        if self.first_node is None:
            return 0

        current_node, length = self.first_node, 1
        while current_node.next is not None:
            length += 1
            current_node = current_node.next
        return length

# TODO Is update_last() needed?
    def update_last(self):
        # Runs through the list nodes for some reason
        new_last = self.first_node
        for _ in range(0, self.length() - 1):
            new_last = new_last.next
        return new_last

    def pop(self, target: int = 0) -> Any:
        """
        Removes a node with a given index from current list
        :param target: Index to remove
        :return: Value of popped element
        """
        length = self.length()
        if length == 0:
            raise IndexError("List is empty")
        elif not isinstance(target, int):
            raise ValueError("Index must be an integer")
        elif target >= length or target < -length:
            raise IndexError("Given index is not in list")

        # Handle edge-case
        if target == 0:
            popped_value = self.first_node.data
            self.first_node = self.first_node.next
            return popped_value

        current_node = self.first_node
        if target > 0:  # Popping a positive index
            # Reach node to remove
            for _ in range(target - 1):
                current_node = current_node.next
            popped_value = current_node.next.data
            current_node.next = current_node.next.next

            # Edge-case of removing last node
            if current_node.next is None:
                self.last_node = current_node  # Update last node

            return popped_value
        # TODO STOPPED HERE
        else:  # Popping a negative index
            if length == 1:
                popped_value = self.first_node.data
                self.clear()
                return popped_value
            elif abs(target) != length:
                for i in range(0, length - 1 - abs(target)):
                    current_node = current_node.next
                popped_value = current_node.next.data
                current_node.next = current_node.next.next
                self.last_node = self.update_last()
                return popped_value
            else:
                popped_value = self.first_node.data
                self.first_node = self.first_node.next
                self.last_node = self.update_last()
                return popped_value

    def reverse(self):  # TODO Can be static, but... What should I do?
        # Literally reverses AND returns a reversed version of MyList
        return Reverse().rev_reverse()

    # ----- Bonus -----

    def count(self, to_search):
        # Returns how many times given value is in MyList
        times_found, current_node = 0, self.first_node
        if current_node.data == to_search:
            times_found += 1
        for i in range(0, self.length() - 1):
            current_node = current_node.next
            if current_node.data == to_search:
                times_found += 1
        return times_found

    def index(self, to_search):
        # Returns the first index of the node with given value
        index, current_node = 0, self.first_node
        if current_node.data == to_search:
            return index
        for i in range(0, self.length() - 1):
            index += 1
            current_node = current_node.next
            if current_node.data == to_search:
                return index
        raise Exception(f"{to_search} {type(to_search)} is not in MyList")

    # TODO insert() function???

    def remove(self, to_remove):
        # Removes a node by given value
        current_node = self.first_node
        if current_node.data == to_remove:
            self.pop(self.index(to_remove))
            return True
        for i in range(0, self.length() - 1):
            current_node = current_node.next
            if current_node.data == to_remove:
                self.pop(self.index(to_remove))
                return True
        raise Exception(f"{to_remove} {type(to_remove)} is not in MyList")

    def clear(self) -> None:
        """
        Removes all nodes from a list
        :return: None
        """
        self.first_node = self.last_node = None


# class Reverse:
#
#     # TODO In the reverse() I'm referencing to "first_list". A problem, right?
#
#     def __init__(self):
#         self.rev_first_node = self.rev_last_node = None
#
#     def rev_append(self, data):
#         node = ListNode(data)
#         if self.rev_length() == 0:
#             self.rev_first_node = self.rev_last_node = node
#         else:
#             self.rev_last_node.next = self.rev_last_node = node
#
#     def rev_length(self):
#         if self.rev_last_node is None:
#             return 0
#         else:
#             current_node, length = self.rev_first_node, 1
#             while current_node.next is not None:
#                 length += 1
#                 current_node = current_node.next
#             return length
#
#     def rev_reverse(self):
#         loop_times = first_list.length()
#         for i in range(0, loop_times):
#             self.rev_append(first_list.pop(-1))
#         first_list.first_node, first_list.last_node = self.rev_first_node, self.rev_last_node
#         return self.rev_first_node


first_list = MyList()
first_list.append(1)
first_list.append("hi")
first_list.append(3.14)
first_list.extend([2, 3])
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}")
print(first_list.pop(4))
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}")
print(f"{first_list.length() = }")

# second_list = MyList()
# print(f"{second_list.length() = }")

# first_list = MyList()  # Create a new list named first_list
# print("Created new list (First_list)\n")
# first_list.append(1)
# print("After append():")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}\n")
# first_list.extend([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# print("After extend():")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}\n")
# print(f"Length of first_list = {first_list.length()}\n")
# first_list.pop(3)
# print("Popped index 3 in first list:")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}\n")
# first_list.pop(-2)
# print("Popped index -2 in first list:")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}\n")
# print(f"Times 8 is in first_list = {first_list.count(8)}\n")
# print(f"First index of \"7\" in MyList = {first_list.index(7)}\n")
# first_list.remove(2)
# print("Removed first node with value 2:")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}\n")
# first_list.reverse()
# print("Reversed MyList:")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}\n")
# first_list.clear()
# print("Cleared MyList")
# print(f"First Node = {first_list.first_node}")
# print(f"Last Node = {first_list.last_node}")
