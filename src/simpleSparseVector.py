class SparseVector:
    """Реализация класса для оптимального хранения разреженного вектора"""
    def __init__(self, vector):
        self.svector = {}

        for i in range(len(vector)):
            if vector[i] != 0:
                self.svector[i] = vector[i]
    
    def __repr__(self) -> str:
        output_string = ""

        for i, val in self.svector.items():
            output_string += f'vector[{i}] == {val}\n'
        
        return output_string

    def scalar(self, other):
        """Вычислить скалярное произведение векторов равной размерности"""
        if len(self.svector) != len(other.svector):
            raise Exception('Векторы имеют различную размерность')

        scal_product = 0
        for i, val in self.svector.items():
            if i in other.svector:
                scal_product += val * other.svector[i]
        
        return scal_product

a = [0, 1, 3, 2, 0, 0, 0, 0, 0, 0, 5, 10]
b = [0, 0, 0, 3, 0, 0, 1, 2, 5, 0, 0, 15]

sa = SparseVector(a)
sb = SparseVector(b)

print(f'Sparse vector:\n{sa}')


print(f'Scalar product of vectors: {sa.scalar(sb)}')