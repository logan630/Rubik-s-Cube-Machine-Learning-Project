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


class RubiksCube:

    rotations = {
        'R': right,
        'R\'': anti_right,
        'F': front,
        'F\'': anti_front,
        'L': left,
        'L\'': anti_left,
        'B': back,
        'B\'': anti_back,
        'U': up,
        'U\'': anti_up,
        'D': down,
        'D\'': anti_down
    }

    def __init__(self):

        self.components = []
        self.frame = []

        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):

                    self.components.append(Cubie(i,j,k))    
                    self.frame[i+1][j+1][k+1] = Cubie(i,j,k)


    def right(self):

        for i in range(len(self.components)):

            if self.components[i].x == 1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Up'] = self.components[i].colors['Front']
                other.colors['Back'] = self.components[i].colors['Up']
                other.colors['Down'] = self.components[i].colors['Back']
                other.colors['Front'] = self.components[i].colors['Down']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other
    

    def anti_right(self):

        for i in range(len(self.components)):

            if self.components[i].x == 1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Front'] = self.components[i].colors['Up']
                other.colors['Up'] = self.components[i].colors['Back']
                other.colors['Back'] = self.components[i].colors['Down']
                other.colors['Down'] = self.components[i].colors['Front']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def front(self):

        for i in range(len(self.components)):

            if self.components[i].y == 1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Up'] = self.components[i].colors['Left']
                other.colors['Right'] = self.components[i].colors['Up']
                other.colors['Down'] = self.components[i].colors['Right']
                other.colors['Left'] = self.components[i].colors['Down']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def anti_front(self):

        for i in range(len(self.components)):

            if self.components[i].y == 1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Left'] = self.components[i].colors['Up']
                other.colors['Up'] = self.components[i].colors['Right']
                other.colors['Right'] = self.components[i].colors['Down']
                other.colors['Down'] = self.components[i].colors['Left']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def left(self):

        for i in range(len(self.components)):

            if self.components[i].x == -1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Front'] = self.components[i].colors['Up']
                other.colors['Up'] = self.components[i].colors['Back']
                other.colors['Back'] = self.components[i].colors['Down']
                other.colors['Down'] = self.components[i].colors['Front']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def anti_left(self):

        for i in range(len(self.components)):

            if self.components[i].x == -1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Up'] = self.components[i].colors['Front']
                other.colors['Back'] = self.components[i].colors['Up']
                other.colors['Down'] = self.components[i].colors['Back']
                other.colors['Front'] = self.components[i].colors['Down']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other


    def back(self):

        for i in range(len(self.components)):

            if self.components[i].y == -1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Left'] = self.components[i].colors['Up']
                other.colors['Up'] = self.components[i].colors['Right']
                other.colors['Right'] = self.components[i].colors['Down']
                other.colors['Down'] = self.components[i].colors['Left']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def anti_back(self):

        for i in range(len(self.components)):

            if self.components[i].y == -1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Up'] = self.components[i].colors['Left']
                other.colors['Right'] = self.components[i].colors['Up']
                other.colors['Down'] = self.components[i].colors['Right']
                other.colors['Left'] = self.components[i].colors['Down']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other


    def up(self):

        for i in range(len(self.components)):

            if self.components[i].z == 1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Front'] = self.components[i].colors['Right']
                other.colors['Left'] = self.components[i].colors['Front']
                other.colors['Back'] = self.components[i].colors['Left']
                other.colors['Right'] = self.components[i].colors['Back']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def anti_up(self):

        for i in range(len(self.components)):

            if self.components[i].z == 1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Right'] = self.components[i].colors['Front']
                other.colors['Front'] = self.components[i].colors['Left']
                other.colors['Left'] = self.components[i].colors['Back']
                other.colors['Back'] = self.components[i].colors['Right']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def down(self):

        for i in range(len(self.components)):

            if self.components[i].z == -1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Right'] = self.components[i].colors['Front']
                other.colors['Front'] = self.components[i].colors['Left']
                other.colors['Left'] = self.components[i].colors['Back']
                other.colors['Back'] = self.components[i].colors['Right']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other

    
    def anti_down(self):

        for i in range(len(self.components)):

            if self.components[i].z == -1:

                other = Cubie(self.components[i].x,self.components[i].y,self.components[i].z)
                other.colors['Front'] = self.components[i].colors['Right']
                other.colors['Left'] = self.components[i].colors['Front']
                other.colors['Back'] = self.components[i].colors['Left']
                other.colors['Right'] = self.components[i].colors['Back']

                self.components[i] = other
                self.frame[other.x+1][other.y+1][other.z+1] = other