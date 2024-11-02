#Step 1: Define the Node Class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




#Step 2: Create the LinkedList Class


class LinkedList:
    def __init__(self):
        self.head = None




#Step 3: Implement the Append Method


class LinkedList:
    # ... (previous code)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)




#Step 4: Implement the Display Method


class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3




#Step 5: Implement the Insert Method


class LinkedList:
    # ... (previous code)

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3



#Step 6: Implement the Delete Method


class LinkedList:
    # ... (previous code)

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3




#Step 7: Implement the Search Method


class LinkedList:
    # ... (previous code)

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1



#Step 8: Implement the Reverse Method

class LinkedList:
    # ... (previous code)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1




#Exercises


# 1.To find the middle element of the linked list.

class LinkedList:

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Middle element:", ll.find_middle()) 



# 2. To detect if the linked list has a cycle.

class LinkedList:

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.head.next.next.next.next.next = ll.head.next  

print("Has cycle:", ll.has_cycle())  

ll_no_cycle = LinkedList()
ll_no_cycle.append(1)
ll_no_cycle.append(2)
ll_no_cycle.append(3)
print("Has cycle:", ll_no_cycle.has_cycle())  


# 3.To remove duplicates from an unsorted linked list.

class LinkedList:

    def remove_duplicates(self):
        if not self.head:
            return
        current = self.head
        seen = set()
        seen.add(current.data)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(1)
ll.append(5)
print("List after removing duplicates:", ll.remove_duplicates())


# 4. To merge two sorted linked lists into a single sorted linked list.

class LinkedList:

    def merge_sorted(self, other_list):
        dummy = Node(0)  
        tail = dummy
        l1, l2 = self.head, other_list.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list
    

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_ll = ll1.merge_sorted(ll2)

print("Merged list:")
merged_ll.display() 