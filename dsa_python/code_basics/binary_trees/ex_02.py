class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    # loud and clear
    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()    
        return elements    
    
    
    
    # solution of exercise
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):
        elements_arr=self.in_order_traversal()
        return sum(elements_arr)






def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


if __name__ == "__main__":
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print("USA In tree?",country_tree.search("USA"))
    print("Guatemala In tree?",country_tree.search("Guatemala"))
    print(country_tree.in_order_traversal())

    numbers_tree = build_tree([5,6])
    print( numbers_tree.find_min())
    print( numbers_tree.find_max())
    print( numbers_tree.calculate_sum())