class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node

        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def remove_from_front(self):
        if self.head == None:
            return self
        self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        test = runner
        runner = self.head
        while runner.next != test:
            runner = runner.next
        runner.next = None
        return self

    def remove_val(self, val):
        if self.head == None:
            return self
        runner = self.head
        while runner.value != val:
            runner = runner.next
        temp = runner
        runner = self.head
        while runner.next != temp:
            runner = runner.next
        runner.next = temp.next
        return self

    def insert_at(self, val, n):
        new_node = SLNode(val)
        if self.head == "":
            self.add_to_front(val)
        else:
            runner = self.head
            count = 1
            while count != n:
                runner = runner.next
                count += 1
            new_node.next = runner.next
            runner.next = new_node
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").insert_at('super', 2).print_values()


