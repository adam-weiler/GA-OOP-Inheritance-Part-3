class System():
    bodies = []
    
    def add(self, celestial_body):
        self.bodies.append(celestial_body)
        return celestial_body

    def total_mass(self):
        return sum(self.bodies)



