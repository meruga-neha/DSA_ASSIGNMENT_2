#1q Delete the elements in an linked list whose sum is equal to zero

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_zero_sum(head):
    current = head
    sum_list = 0
    while current:
        sum_list += current.data
        current = current.next

    if sum_list == 0:
   
        return None
    current = head
    while current:
        temp = current.next
        temp_sum = current.data
        while temp:
            temp_sum += temp.data
            if temp_sum == 0:
              
                current.next = temp.next
                break
            temp = temp.next
        current = current.next

    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
head = Node(6)
head.next = Node(-6)
head.next.next = Node(8)
head.next.next.next = Node(4)
head.next.next.next.next = Node(-12)
head.next.next.next.next.next = Node(9)
print("Original Linked List:")
print_linked_list(head)
head = delete_zero_sum(head)
print("Modified Linked List:")
print_linked_list(head)


#2q Reverse a linked list in groups of given size

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def reverse_in_groups(head,n):
    current = head
    next_node = None
    prev = None
    count = 0
    while current and count < n:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    if next_node:
        head.next = reverse_in_groups(next_node,n)
    return prev
def print_linked_list(head):
    current = head
    while current:
        print(current.data ,end = " ")
        current = current.next
    print()
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
head.next.next.next.next.next = node(6)
head.next.next.next.next.next.next = node(7)
head.next.next.next.next.next.next.next = node(8)
head.next.next.next.next.next.next.next.next = node(9)
head.next.next.next.next.next.next.next.next.next = node(10)
print('orginal linked list')
print_linked_list(head)
n = 3
head = reverse_in_groups(head, n)
print('modified linked list!')
print_linked_list(head)


#3q Merge a linked list into another linked list at alternate positions

class node(object):
    def __init__(self,data:int):
        self.data = data
        self.next = None
class linked_list(object):
    def __init__(self):
        self.head = None
    def push(self,new_data:int):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
    def merge(self,p,q):
        p_curr = p.head
        q_curr = q.head
        while p_curr != None and q_curr != None:
            p_next = p_curr.next
            q_next = q_curr.next
            q_curr.next = q_next
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr
list_1 = linked_list()
list_2 = linked_list()

list_1.push(3)
list_1.push(2)
list_1.push(1)
list_1.push(0)
for i in range(8,3,-1):
    list_2.push(i)
print('first linked list!')
list_1.print_list()
print('second linked list!')
list_2.print_list()

list_1.merge(p=list_1, q=list_2)
  
print('modified first linked list!')
list_1.print_list()
print('modified second linked list!')
list_2.print_list()


#4q In an array, Count Pairs with given sum

def getPairsCount(arr, n, K):
    count = 0  # Initialize result
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                count += 1
 
    return count
arr = list(map(int,input().split()))
n = len(arr)
K = 6
print("Count of pairs is",
      getPairsCount(arr, n, K))
 

#5qFind duplicates in an array

arr = list(map(int,input().split()));     
     
print("Duplicate elements in given array: ");    
#Searches for duplicate element    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);  


#6Find the Kth largest and Kth smallest number in an array

def find_kth_largest_smallest(array,k):
    array.sort()
    kth_largest = array[-k]
    kth_smallest = array[k-1]
    return kth_largest,kth_smallest
array = list(map(int,input('enter the list of array:').split()))
k = int(input('enter k value:'))
largest,smallest = find_kth_largest_smallest(array,k)
print(f"the {k}th largest number in the array is: {largest}")
print(f"the {k}th samllest number in the array is: {smallest}")


#7q Move all the negative elements to one side of the array

def shift_negative_values(arr):
    left = 0
    right = len(arr)- 1
    while left <= right:
        if arr[left]<0 and arr[right] < 0:
            left += 1
        elif arr[left]>=0 and arr[right]<0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        elif arr[left]>=0 and arr[right]>=0:
            right -= 1
        else:
            left += 1
            right -= 1
    return arr
array = list(map(int,input('enter the list of array:').split()))
result = shift_negative_values(array)
print('modified array with negative elements shifted to one side:')
print(result)

#8q Reverse a string using a stack data structure

def create_a_stack():
    stack = []
    return stack
def size(stack):
    return len(stack)
def isempty(stack):
    if size(stack) == 0:
        return True
def push(stack,item):
    stack.append(item)
def pop(stack):
    if isempty(stack):
        return 
    return stack.pop()
def reverse_stack(string):
    n = len(string)
    stack = create_a_stack()
    for i in range(0,n,1):
        push(stack,string[i])
    string = ""
    for i in range(0,n,1):
        string += pop(stack)
    return string
string = input('enter the string:')
string = reverse_stack(string)
print('reversed string is:',string)


#9q Evaluate a postfix expression using stack

class Evaluate:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self, op):
        self.top += 1
        self.array.append(op)
    def evaluate_Postfix(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("postfix evaluation: %d" % (obj.evaluate_Postfix(exp)))


#10q Implement a queue using the stack data structure


class queue:
    def __init__(self):
        self.in_stack =[]
        self.out_stack = []
    def enqueue(self,item):
        self.in_stack.append(item)
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                if not self.out_stack:
                    return None
                return self.out_stack.pop()
    def is_empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
    def size(self):
        return len(self.in_stack) + len(self.out_stack)
queue_1 = queue()
queue_1.enqueue(1)
queue_1.enqueue(2)
queue_1.enqueue(3) 
print(f"queue size: {queue_1.size()}")
print(queue_1.dequeue())
print(queue_1.dequeue())
queue_1.enqueue(4)
queue_1.enqueue(5)
print(queue_1.dequeue())
print(queue_1.dequeue())
print(queue_1.dequeue())
print(queue_1.dequeue())
print(f"is queue empty?{queue_1.is_empty()}")

