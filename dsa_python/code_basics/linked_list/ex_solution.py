# Assignments Solved Given By Codebasics

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Now the main class linked list


class LinkedList:
    def __init__(self):
        self.head = None

    # deffining the print of linked list
    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        lst_data = ""
        while itr:
            lst_data += str(itr.data) + " <--> "
            itr = itr.next
        return lst_data

    # getting the length of a linked list
    def get_length(self):
        len = 0
        itr = self.head
        # as itr updates to itr.next so itr autometically equals to none
        while itr:
            len += 1
            itr = itr.next
        return len

    # linked list insertion method
    def insert_at_first(self, data):
        if data:
            if self.head:
                prev_data = self.head
                new_data_node = Node(data)
                self.head = new_data_node
                self.head.next = prev_data
                return
            else:
                self.head = Node(data)
                return
        else:
            raise Exception("not a valid data")

    # insert at last
    def insert_at_last(self, data):
        if data:
            if self.head:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(data)
                return
            self.head = Node(data)
        else:
            raise Exception("not a valid data")
    
    # inserting data at specific index 
    def insert_at(self, index, data):
        if data:
            # checking the index
            if index > 0 and index < self.get_length():
                itr = self.head
                curr_idx = 0
                while itr:
                    if curr_idx == index-1:
                        prev_node_ref = itr.next
                        itr.next = Node(data)
                        itr.next.next = prev_node_ref
                    # upgradation
                    curr_idx += 1
                    itr = itr.next
                return
            else:
                raise Exception("invalid index")

        else:
            raise Exception("not a valid data")
        
    # remmoving data at given inddex   
    def remove_at(self, index):
        if index ==0:
            self.head=self.head.next
            return
        if index > 0 and index < self.get_length():
                itr = self.head
                curr_idx = 0
                while itr:
                    if curr_idx == index-1:
                        itr.next = itr.next.next
                    # upgradation
                    curr_idx += 1
                    itr = itr.next
                return
        else:
            raise Exception("invalid index")
    # insert values from list/arr
    def insert_values(self , datas):
        if type(datas) is list:
            for data in datas :
                self.insert_at_last(data)


    # Assignment Questions

    def find_index(self,value):
        itr = self.head 
        count = 0
        while itr:
            if itr.next==None and value != itr.data:
                return None
            if value == itr.data:
                return count
                    
            # update
            count+=1
            itr=itr.next    



    def insert_after_value(self,value,data):
        if data:
            itr = self.head 
            while itr:
                if itr.next==None and value != itr.data:
                    raise Exception("value not found")
                if value == itr.data:
                    prev_node_ref=itr.next
                    itr.next=Node(data)
                    itr.next.next=prev_node_ref
                    return
                    
                # update
                itr=itr.next
        else:
            raise Exception("not a valid data")
            return
    def remove_by_value(self,value):
        idx=self.find_index(value)
        if idx is not None:
            self.remove_at(idx)
            return
        raise Exception("value not found")



# previewing the linked list
if __name__ == "__main__":
    lst = LinkedList()
    lst.insert_at_first("Mou")
    lst.insert_at_first("Sayed")
    # lst.insert_at_last("Third")
    # lst.insert_at_last("Fourth")
    # lst.insert_at_last("Fifth")
    # lst.insert_at(2, "inserted")
    # lst.insert_at(4,"r")
    # lst.remove_at(2)
    # lst.remove_at(8)
    # lst.insert_values(["sayed",'mou',"mOu"])
    # print(lst.get_length())
    # lst.insert_at_last("hi")
    # lst.insert_after_value("Mou","No One Can Replace Mou")
    # lst.insert_after_value("fdgsg","No One Can Replace Mou")
    # print(lst.print())


    # assignment test
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    print(ll.print())
    ll.insert_after_value("mango","apple") # insert apple after mango
    print(ll.print())
    print("First Call Remove By Value")
    ll.remove_by_value("orange") # remove orange from linked list
    print(ll.print())
    # ll.remove_by_value("figs")
    print("Second Call Remove By Value")
    print(ll.print())
    print(ll.find_index("banana"))
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print(ll.print())





# simple function for making pattern