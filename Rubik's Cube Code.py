class Cubie:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

        self.colors = {
            'Up': 'White',
            'Front': 'Green',
            'Down': 'Yellow',
            'Back': 'Blue',
            'Left': 'Orange',
            'Right': 'Red'
        }

    def __eq__(self, other):

        return self.colors == other.colors

    def check_equal_position(self, other):

        correct_x = self.x == other.x 
        correct_y = self.y == other.y 
        correct_z = self.z == other.z 

        return correct_x and correct_y and correct_z

#what up dawg
class RubiksCube:

    def __init__(self):

        self.components = []

        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):

                    self.components.append(Cubie(i,j,k))    