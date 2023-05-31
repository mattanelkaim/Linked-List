# TODO remove() the returns..

class ListNode:
    def __init__(self, data):
        self.data, self.next = data, None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return f"(data={str(self.data)}, next={str(self.next)})"


class MyList:
    def __init__(self):
        # Initializes an empty list
        self.first_node = self.last_node = None

    def append(self, data):
        # Create a new ListNode object and add it to the list
        node = ListNode(data)
        if self.length() == 0:
            self.first_node = self.last_node = node
        else:
            self.last_node.next = self.last_node = node

    def extend(self, other_list):
        # Appends each item in other_list
        for i in other_list:
            self.append(i)

    def length(self):
        # Get the length of MyList
        if self.first_node is None:
            return 0
        else:
            current_node, length = self.first_node, 1
            while current_node.next is not None:
                length += 1
                current_node = current_node.next
            return length

# TODO Is a function of update_last() needed?
    def update_last(self):
        new_last = self.first_node
        for i in range(0, self.length() - 1):
            new_last = new_last.next
        return new_last

    def pop(self, tbp):  # tbp = To Be Popped
        # Removes a node from MyList by given index
        if self.length() == 0:
            raise Exception("MyList is empty")
        elif type(tbp) != int:
            raise Exception("Must be given an integer")
        elif tbp > self.length() - 1 or tbp < -self.length():  # TODO abs(tbp) > self.length()
            raise Exception("Given index is not in MyList")
        else:
            current_node = self.first_node
            if tbp == 0:
                to_return = self.first_node.data
                self.first_node = self.first_node.next
                self.last_node = self.update_last()
                return to_return
            elif tbp > 0:  # If popping a positive index
                for i in range(0, tbp - 1):
                    current_node = current_node.next
                to_return = current_node.next.data
                current_node.next = current_node.next.next
                self.last_node = self.update_last()
                return to_return
            else:  # If popping a negative index
                if self.length() == 1:
                    to_return = self.first_node.data
                    self.clear()
                    return to_return
                elif abs(tbp) != self.length():
                    for i in range(0, self.length() - 1 - abs(tbp)):
                        current_node = current_node.next
                    to_return = current_node.next.data
                    current_node.next = current_node.next.next
                    self.last_node = self.update_last()
                    return to_return
                else:
                    to_return = self.first_node.data
                    self.first_node = self.first_node.next
                    self.last_node = self.update_last()
                    return to_return

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

    def clear(self):
        # Literally clears MyList
        self.first_node = self.last_node = None


class Reverse:

    # TODO In the reverse() I'm referencing to "first_list". A problem, right?

    def __init__(self):
        self.rev_first_node = self.rev_last_node = None

    def rev_append(self, data):
        node = ListNode(data)
        if self.rev_length() == 0:
            self.rev_first_node = self.rev_last_node = node
        else:
            self.rev_last_node.next = self.rev_last_node = node

    def rev_length(self):
        if self.rev_last_node is None:
            return 0
        else:
            current_node, length = self.rev_first_node, 1
            while current_node.next is not None:
                length += 1
                current_node = current_node.next
            return length

    def rev_reverse(self):
        loop_times = first_list.length()
        for i in range(0, loop_times):
            self.rev_append(first_list.pop(-1))
        first_list.first_node, first_list.last_node = self.rev_first_node, self.rev_last_node
        return self.rev_first_node


first_list = MyList()  # Create a new list named first_list
print("Created new list (First_list)\n")
first_list.append(1)
print("After append():")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}\n")
first_list.extend([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print("After extend():")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}\n")
print(f"Length of first_list = {first_list.length()}\n")
first_list.pop(3)
print("Popped index 3 in first list:")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}\n")
first_list.pop(-2)
print("Popped index -2 in first list:")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}\n")
print(f"Times 8 is in first_list = {first_list.count(8)}\n")
print(f"First index of \"7\" in MyList = {first_list.index(7)}\n")
first_list.remove(2)
print("Removed first node with value 2:")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}\n")
first_list.reverse()
print("Reversed MyList:")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}\n")
first_list.clear()
print("Cleared MyList")
print(f"First Node = {first_list.first_node}")
print(f"Last Node = {first_list.last_node}")
