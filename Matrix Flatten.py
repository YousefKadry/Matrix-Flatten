import ast

class matrix3D_flatten:

    def  __init__(self, matrix_3D):
        self.vector_1D = []
        self.matrix = matrix_3D
        self.width = len(matrix_3D)
        self.hight = len(matrix_3D[0])
        self.depth = len(matrix_3D[0][0])


    def flatten(self):
        for matrix_2D in self.matrix:
            for matrix_1D in matrix_2D:
                for elem in matrix_1D:
                    self.vector_1D.append(elem)
        return self.vector_1D


    def get_elem(self, i, j, k):
        if (i<self.width and j<self.hight and k<self.depth):
            elem_index = k + j*self.depth + i*self.depth*self.hight
            return self.vector_1D[elem_index]
        else:
            raise Exception("invalid index")


if __name__ == '__main__':

    while(True):
        matrix_3D = input('enter 3D matrix: ')
        # matrix_3D = '[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]'


        try:
            matrix_3D = ast.literal_eval(matrix_3D)
            flattend_matrix = matrix3D_flatten(matrix_3D)
            vector = flattend_matrix.flatten()
            print(vector)
        except:
            print('invalid input.\nplease, enter 3D matrix.')
            continue

        while (True):
            try:
                x, y, z = input('enter index: \n').split()
                print(flattend_matrix.get_elem(int(x), int(y), int(z)))
                # for testing
                # print(matrix_3D[int(x)][int(y)][int(z)])
                break
            except:
                print('invalid input.\nplease, enter valid index.')


    
