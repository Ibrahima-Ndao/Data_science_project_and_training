class Noeud:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class ArbreBinaire:
    def __init__(self):
        self.root = None
        
    def createTree(self):
        one = Noeud(1)
        two = Noeud(2)
        three = Noeud(3)
        four = Noeud(4)
        five = Noeud(5)
        self.root = one
        one.left = two
        one.right = three
        two.left = four
        two.right = five
        
    def prefixerecursif(self, p):
        if p == None:
            return
        else:
            print(p.data, end=' ')
            self.prefixerecursif(p.left)
            self.prefixerecursif(p.right)
            
    def prefixeiteratif(self, p):
        pile = []
        while p != None or len(pile) != 0:
            while p != None:
                print(p.data, end=' ')
                pile.append(p)
                p = p.left
            if len(pile) != 0:
                p = pile.pop()
                p = p.right
                
    def prefixiteratif(self, p):
        pile = []
        while p != None or len(pile) != 0:
            while p != None:
                print(p.data, end=' ')
                pile.append(p)
                p = p.left
            p = pile.pop()
            p = p.right
            
    def topologieIterative(self, p):
        n = 0
        ng = 0
        nd = 0
        nf = 0
        ni = 0
        pile = []
        cg = ''
        cd = ''
        cf = ''
        ci = ''
        while p is not None or len(pile) != 0:
            if p is not None:
                n = n + 1
                if p.left is None and p.right is None:
                    nf = nf + 1
                    cf = cf + ' ' + str(p.data)
                if (p != self.root) and (p.left is not None or p.right is not None):
                    ni = ni + 1
                    ci = ci + ' ' + str(p.data)
                pile.append(p)
                p = p.left
                if p is not None:
                    ng = ng + 1
                    cg = cg + ' ' + str(p.data)
                else:
                    p = pile.pop()
                    p = p.right
                    if p is not None:
                        nd = nd + 1
                        cd = cd + ' ' + str(p.data)
    
        print('Nombre de noeuds :', n)
        print('Nombre de feuilles :', nf)
        print('Chemin de feuilles :', cf)
        print('Nombre de noeuds internes :', ni)
        print('Chemin de noeuds internes :', ci)
        print('Nombre de noeuds à gauche :', ng)
        print('Chemin gauche :', cg)
        print('Nombre de noeuds à droite :', nd)
        print('Chemin droite :', cd)
        
    def compteNoeud(self, p):
        if p == None:
            return 0
        else:
            return 1 + self.compteNoeud(p.left) + self.compteNoeud(p.right)
            
    def comptefeuilles(self, p):
        if p == None:
            return 0
        else:
            if p.left == None and p.right == None:
                return 1
            else:
                return self.comptefeuilles(p.left) + self.comptefeuilles(p.right)
    def cheminFeuilles(self, p):
        if p == None:
            return ''
        else: 
            if p.left == None and p.right == None:
                return ' ' + str(p.data)
            else:
                return self.cheminFeuilles(p.left) + self.cheminFeuilles(p.right)

def main():
    ab = ArbreBinaire()
    ab.createTree()
    print("Recursive Preorder Traversal:")
    ab.prefixerecursif(ab.root)
    print("\nIterative Preorder Traversal: (1)")
    ab.prefixeiteratif(ab.root)
    print("\nIterative Preorder Traversal: (2)")
    ab.prefixiteratif(ab.root) 
    print("\nIterative Preorder Traversal: (3)")
    ab.topologieIterative(ab.root)
    n = ab.compteNoeud(ab.root)
    print('Nombre noeud en recursif : ', n)
    nf = ab.comptefeuilles(ab.root)
    print('nombre feuilles en récursif : ', nf)
    print('Chemin feuilles récursif :', ab.cheminFeuilles(ab.root))
main()
