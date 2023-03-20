#
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
#
#      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#              Buddha bless        No Bugs

class XC3_tree:
    def __init__(self, degree):
        self.degrees = degree
        self.children = []
        self.init_tree(self.degrees)

    def init_tree(self,degree):
        for i in range(1,degree+1):
            if (i>2):
                self.children.append(XC3_tree(i-2))
            else:
                self.children.append(XC3_tree(0))
    def degree(self):
        return self.degrees

    def Height(self):
        if (self.degrees == 0):
            return 1
        else:
            return 1+ max(child.Height() for child in self.children)
    def Nodes(self):
        if (self.degrees == 0):
            return 1
        else:
            return 1 + sum(child.Nodes() for child in self.children)
    def info(self):
        return f"XC3 Tree with {self.degrees} degrees and Height: {self.Height()} and Nodes: {self.Nodes()}"

def h(i):
    TheTREEE = XC3_tree(i)
    return TheTREEE.Height()
def nodes(i):
    TREE = XC3_tree(i)
    return TREE.Nodes()

def exp3():
    list = []
    for i in range (26):
        tree = XC3_tree(i)
        list.append(h(i))
    print(*list)

def exp4():
    list = []
    for i in range (26):
        tree = XC3_tree(i)
        list.append(nodes(i))
    print(*list)


root = XC3_tree(7)
#print(root.info())
#print(h(7))
#print(nodes(7))
exp3() #height: 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14
exp4() #nodes:  1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418

