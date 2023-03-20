import matplotlib.pyplot as plot
import random
from time import time
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def find_height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.find_height(node.left)
            right_height = self.find_height(node.right)
            return max(left_height, right_height) + 1


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
        #x.left = z
        #x.parent = z.parent
        x.parent = self.parent
        if self.parent != None:
            if self == self.parent.left:
                self.parent.left = x
            else:
                self.parent.right = x
        x.right = self
        self.parent = x
        #x.make_black()
        #self.parent.parent.make_red()
        

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
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red():
            if node.parent.is_left_child():
                if node.parent.parent.right != None:
                    if node.parent.parent.right.is_red():
                        node.parent.make_black()
                        node.parent.parent.right.make_black()
                        node.parent.parent.make_red()
                        node = node.parent.parent
                    else:
                        if node.is_right_child():
                            node = node.parent
                            if node == self.root:
                                self.root = node.right
                            node.rotate_left()
                        
                        else:
                            node.parent.make_black()
                            node.parent.parent.make_red()
                            if node.parent.parent == self.root:
                                self.root = node.parent.parent.left
                            node.parent.parent.rotate_right()
                            
                else:
                    if node.is_right_child():
                            node = node.parent
                            if node == self.root:
                                self.root = node.right
                            node.rotate_left()
                        
                    else:
                        node.parent.make_black()
                        node.parent.parent.make_red()
                        if node.parent.parent == self.root:
                            self.root = node.parent.parent.left
                        node.parent.parent.rotate_right()

            else:
                if node.parent.parent.left != None:
                    if node.parent.parent.left.is_red():
                        node.parent.make_black()
                        node.parent.parent.left.make_black()
                        node.parent.parent.make_red()
                        node = node.parent.parent
                    
                    else:
                        if node.is_left_child():
                            node = node.parent
                            if node == self.root:
                                self.root = node.left
                            node.rotate_right()
                    
                        else:
                            node.parent.make_black()
                            node.parent.parent.make_red()
                            if node.parent.parent == self.root:
                                self.root = node.parent.parent.right
                            node.parent.parent.rotate_left()
                            
                else:
                        if node.is_left_child():
                            node = node.parent
                            if node == self.root:
                                self.root = node.left
                            node.rotate_right()
                    
                        else:
                            node.parent.make_black()
                            node.parent.parent.make_red()
                            if node.parent.parent == self.root:
                                self.root = node.parent.parent.right
                            node.parent.parent.rotate_left()

        self.root.make_black()
                    
        
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
    
def generate_list(length,max_value):
    return [random.randint(0, max_value) for _ in range(length)]
def swap(L,i,j):
    L[i], L[j] = L[j], L[i]
def create_near_sorted_list(length, max_value, swaps):
    L = generate_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def print_vertical_tree(node, level=0):
    if node is not None:
        print_vertical_tree(node.right_child, level+1)
        print('   '*level + '|__' + str(node.value))
        print_vertical_tree(node.left_child, level+1)

def experiment1(runs):
    percent =0 
    rbt_sum=0
    bst_sum=0
    for i in range(runs):
        percent +=1
        print("percentage : ", percent )
        lst = generate_list(10000,100)
        rbt = RBTree()
        bst = BST()
        for num in lst:
            rbt.insert(num)
            bst.insert(num)
        rbt_height = rbt.get_height()
        bst_height = bst.find_height(bst.root)
        rbt_sum= rbt_sum + rbt_height
        bst_sum=bst_sum + bst_height
    rbtbybst = rbt_sum/bst_sum
    bstbyrbt= bst_sum/rbt_sum
    if rbtbybst>1:
        print("RBT height is larger by : " ,rbtbybst)
    elif bstbyrbt>1:
        print("BST height is larger by : " ,bstbyrbt)

def experiment2(runs):
    percent =0 
    swaps = 100
    swp=0
    swaps_list =[]
    total_rbt_minus_bst= []
    total_bst_minus_rbt= []
    for i in range(runs):
        percent+=1
        print("percent is :" ,percent)
        for i in range(swaps):
            if(i%1==0):
                swp+=1
            swaps_list.append(swp)
            L1 = create_near_sorted_list(100,100,i)
            rbt = RBTree()
            bst = BST()
            for num in L1:
                rbt.insert(num)
                bst.insert(num)
            rbt_height = rbt.get_height()
            bst_height = bst.find_height(bst.root)
            difference_of_rbt_bst= rbt_height-bst_height
            difference_of_bst_rbt= bst_height-rbt_height
            total_bst_minus_rbt.append(difference_of_bst_rbt)
            total_rbt_minus_bst.append(difference_of_rbt_bst)
    ax = plot.gca()
    ax.set_xlim([0,swaps])
    ax.set_ylim([-100,100])
    plot.plot(swaps_list,total_bst_minus_rbt, label="height(bst)-height(rbt)") 
    plot.plot(swaps_list,total_rbt_minus_bst, label = "height(rbt)-height(bst)") 
    plot.legend(loc="upper left")
    plot.xlabel("Amount of swaps: ")
    plot.ylabel("difference in the lenght of trees")
    plot.title("Experiment 2")
    plot.show()

