class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,tree) -> None:
        tree.parent=self
        self.children.append(tree)


    def add_multiple_child(self,childs):
        for child in childs:
            self.add_child(child)

    def get_level(self):
        start_level=0
        p = self.parent
        while p:
            start_level+=1
            p=p.parent
        return start_level
    
    def print_tree(self ,print_type):
        spaces  = " "*self.get_level()*3
        prefix = spaces + "|___" if self.get_level() else ""

        if print_type.lower() == "both":
            print(prefix+self.data[0]+f"({self.data[1]})")
            
        elif print_type.lower() == "name":

            print(prefix+self.data[0])
        elif print_type.lower()=="designation":
            print(prefix+self.data[1])




        if self.children:
            for child in self.children:
                child.print_tree(print_type)


# adding the child in tree
def tree_operation():
    # root = TreeNode("Electronics")

    # laptop = TreeNode("Laptop")
    # laptop.add_child(TreeNode("Mac"))
    # laptop.add_child(TreeNode("Surface"))
    # laptop.add_child(TreeNode("Thinkpad"))

    # cellphone = TreeNode("Cell Phone")
    # cellphone.add_child(TreeNode("iPhone"))
    # cellphone.add_child(TreeNode("Google Pixel"))
    # cellphone.add_child(TreeNode("Vivo"))

    # tv = TreeNode("TV")
    # tv.add_child(TreeNode("Samsung"))
    # tv.add_child(TreeNode("LG"))

    # root.add_child(laptop)
    # root.add_child(cellphone)
    # root.add_child(tv)

    root=TreeNode(["Nipul","CEO"])
    
    cto=TreeNode(["Chinmay","CTO"])
    hr_head=TreeNode(["Gels","HR Head"])
    

    ifhead=TreeNode(["Vishwa","Infrustructure Head"])
    app_head=TreeNode(["Aamir","Application Head"])
    rm=TreeNode(["Peter","Recruitment Manager"])
    policy_m=TreeNode(["Waqas","Policy Manager"])

    cloudm=TreeNode(["Dhaval","Cloud Manager"])
    app_manager=TreeNode(["Abhijit","App Manager"])

    # adding ceos child
    root.add_multiple_child([cto,hr_head])

    # adding ctos child
    cto.add_child(ifhead)

    # adding infrustructure head child
    ifhead.add_multiple_child([cloudm,app_manager])

    # adding hr head child
    hr_head.add_multiple_child([rm,policy_m])
    

    # root.print_tree()
    # testing with davals code
    root.print_tree("name") # prints both (name and designation) hierarchy.print_tree("name") # prints only name hierarchy
    root.print_tree("designation") # prints only designation hierarchy
    root.print_tree("both") # prints both (name and designation) hierarchy

if __name__ == "__main__":
    tree_operation()



