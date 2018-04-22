from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
            ##extending to add boolean function
        elif i not in ['+', '-', '*', '/', ')','>','<','==','!']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
            #extending to add boolean function
        elif i in ['+', '-', '*', '/','>','<','==','!',')']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
            
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 3 == 2 ) )")