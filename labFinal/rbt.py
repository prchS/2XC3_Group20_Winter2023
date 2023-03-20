class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return
    
    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"
    
    def rotate_right(self):
        x = self.left
        y = x.right
        
        self.left = y
        if(y!=None):
            y.parent = self

        x.parent = self.parent
        if self.parent != None:
            if self == self.parent.left:
                self.parent.left = x
            else:
                self.parent.right = x
        x.right = self
        self.parent = x
        
    def rotate_left(self):
        x = self.right
        y = x.left

        self.right = y
        if(y!=None):
            y.parent = self

        x.parent = self.parent
        if self.parent != None:
            if self == self.parent.left:
                self.parent.left = x
            else:
                self.parent.right = x
        x.left = self
        self.parent = x


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        if node.parent == None:
            node.make_black()

        while node != None and node.parent != None and node.parent.is_red():
            if node.parent.is_left_child():     # if parent is a left child
                if node.parent.parent.right != None:     # if uncle exists
                    if node.parent.parent.right.is_red():     # if uncle is red
                        node.parent.make_black()
                        node.parent.parent.right.make_black()
                        node.parent.parent.make_red()
                        node = node.parent.parent

                    else:     # if uncle is black
                        if node.is_right_child():     # if node is a right child
                            node = node.parent
                            if node == self.root:     # updates the root if it changes during rotation
                                self.root = node.right
                            node.rotate_left()
                        
                        else:     # if node is a left child
                            node.parent.make_black()
                            node.parent.parent.make_red()
                            if node.parent.parent == self.root:     # updates the root if it changes during rotation
                                self.root = node.parent.parent.left
                            node.parent.parent.rotate_right()
                            
                else:     # uncle does not exists, we assume uncle is black
                    if node.is_right_child():     # if node is a right child
                            node = node.parent
                            if node == self.root:     # updates the root if it changes during rotation
                                self.root = node.right
                            node.rotate_left()
                        
                    else:     # if node is a left child
                        node.parent.make_black()
                        node.parent.parent.make_red()
                        if node.parent.parent == self.root:     # updates the root if it changes during rotation
                            self.root = node.parent.parent.left
                        node.parent.parent.rotate_right()

            else:     # if parent is a right chiild
                if node.parent.parent.left != None:     # if uncle exists
                    if node.parent.parent.left.is_red():     # if uncle is red
                        node.parent.make_black()
                        node.parent.parent.left.make_black()
                        node.parent.parent.make_red()
                        node = node.parent.parent
                    
                    else:     # if uncle is black
                        if node.is_left_child():     # if node is a left child
                            node = node.parent
                            if node == self.root:     # updates the root if it changes during rotation
                                self.root = node.left
                            node.rotate_right()
                    
                        else:     # if node is a right child
                            node.parent.make_black()
                            node.parent.parent.make_red()
                            if node.parent.parent == self.root:     # updates the root if it changes during rotation
                                self.root = node.parent.parent.right
                            node.parent.parent.rotate_left()
                            
                else:     # uncle does not exists, we assume uncle is black
                        if node.is_left_child():     # if node is a left child
                            node = node.parent
                            if node == self.root:     # updates the root if it changes during rotation
                                self.root = node.left
                            node.rotate_right()
                    
                        else:     # if node is a right child
                            node.parent.make_black()
                            node.parent.parent.make_red()
                            if node.parent.parent == self.root:     # updates the root if it changes during rotation
                                self.root = node.parent.parent.right
                            node.parent.parent.rotate_left()

        self.root.make_black()     # the root of a tree should always be black
                    

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Some Test Cases for red-black tree implementation -------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Test-1

# uncomment the code to run.

'''
rbt = RBTree()
rbt.insert(3)
print(rbt,"3")
rbt.insert(1)
print(rbt,"1")
rbt.insert(5)
print(rbt,"5")
rbt.insert(7)
print(rbt,"7")
rbt.insert(6)
print(rbt,"6")
rbt.insert(8)
print(rbt,"8")
rbt.insert(9)
print(rbt,"9")
rbt.insert(10)
print(rbt,"10")'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Test-2

# uncomment the code to run.

'''
rbt = RBTree()
rbt.insert(7)
print(rbt,"7")
rbt.insert(9)
print(rbt,"9")
rbt.insert(6)
print(rbt,"6")
rbt.insert(4)
print(rbt,"4")
rbt.insert(5)
print(rbt,"5")'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Test-3

# uncomment the code to run.

'''
rbt = RBTree()
rbt.insert(10)
print(rbt,"10")
rbt.insert(12)
print(rbt,"12")
rbt.insert(8)
print(rbt,"8")
rbt.insert(9)
print(rbt,"9")
rbt.insert(5)
print(rbt,"5")
rbt.insert(6)
print(rbt,"6")
rbt.insert(4)
print(rbt,"4")
rbt.insert(3)
print(rbt,"3")'''

#----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------