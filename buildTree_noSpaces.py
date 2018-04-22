from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    
    
    ##code so you don't need to uses spaces to split the fpexp
    fplist = []
    numberinstring = ""
        
    for token in fpexp:
        if(token not in ['(','+', '-', '*', '/',')']):
            numberinstring = numberinstring + token
        if token == "(":
            fplist.append(token)
        
        if token in ['(','+', '-', '*', '/',')']:
            if token == '*':
                fplist.append(token)
            if(numberinstring != ""):
                fplist.append(numberinstring)
                numberinstring = ""
                fplist.append(token)

    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
            
        else:
            raise ValueError
    return eTree

##withoutSpaces
pt = buildParseTree("((10+5)*3)")

    