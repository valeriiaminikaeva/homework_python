class Matrix:
    def init(self, matrix):
        self.matrix = matrix
        self.marker = False
        k = 0
        for i in range(len(matrix)):
            if len(self.matrix[0]) == len(self.matrix[i]):
                k += 1
        if k == len(self.matrix):
            self.marker = True
        else:
            print("Матрица некорректнa")

    def trans(self):
        if self.marker:
            n = len(self.matrix)
            m = len(self.matrix[0])
            for i in range(m):
                for j in range(n):
                    print(self.matrix[j][i], end=' ')
                print()


matrix1 = Matrix([[6, 2, 3], [1, 5, 3], [5, 8, 5], [3, 2, 5]])
matrix1.trans()