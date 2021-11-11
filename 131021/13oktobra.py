class Matrica:
    def __init__(self, mat):
        self.mat = mat
        self.g = False
        z = 0
        for u in range(len(mat)):
            if len(self.mat[0]) == len(self.mat[u]):
                z += 1
        if z == len(self.mat):
            self.g = True
        else:
            print("Некорректная матрица")

    def trans(self):
        if self.g:
            q = len(self.mat)
            w = len(self.mat[0])
            for u in range(w):
                for o in range(q):
                    print(self.mat[o][u], end=' ')
                print()


mat1 = __init__ Matrica([[2,3,1,4], [4,5,6,7], [7, 8, 9,0], [1,3,2,1]])
mat1.trans()