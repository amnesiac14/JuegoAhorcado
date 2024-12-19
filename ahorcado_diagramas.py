class Diagramas:
    def intento_0(self):
        return('''    
                    +-------+
                    |       |
                            |
                            |
                            |
                            |
                    ================''')
    
    def intento_1(self):
        return('''    
                    +-------+
                    |       |
                    O       |
                            |
                            |
                            |
                    ================''')
    
    def intento_2(self):
        return('''    
                    +-------+
                    |       |
                    O       |
                   ( )      |
                            |
                            |
                    ================''')
    
    def intento_3(self):
        return('''    
                    +-------+
                    |       |
                    O       |
                  /( )      |
                            |
                            |
                    ================''')
    
    def intento_4(self):
        return('''    
                    +-------+
                    |       |
                    O       |
                  /( )\     |
                            |
                            |
                    ================''')
    
    def intento_5(self):
        return('''    
                    +-------+
                    |       |
                    O       |
                  /( )\     |
                   /        |
                            |
                    ================''')
    
    def intento_6(self):
        return('''    
                    +-------+
                    |       |
                    O       |
                  /( )\     |
                   / \      |
                            |
                    ================''')
    
    #Este método nos será útil para acceder a estos métodos, creados para esta clase, según el intento
    def setIntento(self, num):
        intentos = [self.intento_0, self.intento_1, self.intento_2, self.intento_3, self.intento_4, self.intento_5, self.intento_6]
        return intentos[num]

