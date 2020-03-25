class Node:
    def __init__(self,data=None,left=None ,right =None):
        self.data = data
        self.left = left
        self.right = right
class Tree:
    
    def __init__(self,root=None):
        self.root=root
        self.count=0
        self.countLeft =0
        self.countRight=0
        
    def insert(self,data):
        nn = Node(data)
        if self.root== None:
            self.root = nn

        else:
            temp=self.root
            parent =None
            while temp!=None:
                parent = temp
                if(data<temp.data):
                    temp=temp.left
                elif(data>temp.data):
                    temp= temp.right
            if(data<parent.data):
                    parent.left = nn
            else:
                parent.right=nn
                
    def printtreeIn(self,p):
        temp = p
        if temp!=None:
            Tree.printtreeIn(self,temp.left)
            print(temp.data)      
            Tree.printtreeIn(self,temp.right)
    def printtreePre(self,p):
        temp = p
        if temp!=None:
            print(temp.data)
            Tree.printtreePre(self,temp.left)
            Tree.printtreePre(self,temp.right)
            
    def printtreePost(self,p):
        temp = p
        if temp!=None:
            Tree.printtreePost(self,temp.left)
            Tree.printtreePost(self,temp.right)
            print(temp.data)



    def size(self,p):
        
        if p!= None:
            self.count +=1
            Tree.size(self,p.left)
            Tree.size(self,p.right)

        return self.count


    def maxdepth(self,p):
        if p!=None:
            ldepth =Tree.maxdepth(self,p.left)
            rdepth = Tree.maxdepth(self,p.right)

            if(ldepth>rdepth):
                return ldepth+1
            else:
                return rdepth+1
        else:
            return 0;




    def delete(self,p,data):
        if self.root == None:
            print('Tree is empty')
        if p.left == None and p.right ==None:
            self.root =None
            return p.data
        if p.data>data:
            p.left =Tree.delete(self,p.left,data)

        elif p.data<data:
            p.right = Tree.delete(self,p.right,data)
        
        else:
            if not p.right:
                return p.left
            if not p.left:
                return p.right
            temp = p.right
            minVal = temp.data
            while temp.left:
                temp= temp.left
                minVal = temp.data

            p.val = minVal

            p.right = Tree.delete(self,p.right,p.val)

        return p


                
ob = Tree()
ob.insert(5)
ob.insert(6)
ob.insert(3)
ob.insert(7)
ob.insert(2)
ob.insert(65)
ob.insert(1)
ob.insert(4)
ob.insert(10)
print('inorder')
ob.printtreeIn(ob.root)
print('preorder')
ob.printtreePre(ob.root)
print('postorder')
ob.printtreePost(ob.root)

n = ob.size(ob.root)
print('size=',n)



depth = ob.maxdepth(ob.root)
print(depth)

res = ob.delete(ob.root,9)
print(res)
print('inorder')
ob.printtreeIn(ob.root)
