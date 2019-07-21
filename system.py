class System():
    all_bodies = [] #Stores all bodies from every solar system.

    def __init__(self, name):
        self.name = name
        self.bodies = [] #Stores only bodies from this solar system.

    def __str__(self):
        return f'The {self.name} system.'
    
    def add(self, celestial_body):
        if celestial_body not in self.bodies: #Checks if celestial_body is not in the bodies list yet.
            System.all_bodies.append(celestial_body)
            self.bodies.append(celestial_body)
            return f'Adding {celestial_body.name} to the {self.name} system.'
        else:
            return f'You can\'t add {celestial_body.name} again.'

    def list_all(self, body_type):
        for body in self.bodies: #Iterates through each body in self.bodies list.
            if isinstance(body, body_type): #If current body is of body_type. ie: Planet.
                print(body) #Prints the class-specific __str__ method.

    @classmethod
    def total_mass(cls):
        total_mass = 0

        for body in cls.all_bodies:
            total_mass += body.mass

        return total_mass


class Body():
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    @classmethod
    def list_all(self, body_type):
        for body in System.bodies: #Iterates through each body in System.bodies list.
            if isinstance(body, body_type): #If current body is of body_type. ie: Planet.
                print(body) #Prints the class-specific __str__ method.


class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

    def __str__(self):
        return f'-{self.name} : {self.day} hours per day - {self.year} days per year - weighs {self.mass} kg.'


class Star(Body):
    def __init__(self, name, mass, star_type):
        super().__init__(name, mass)
        self.star_type = star_type

    def __str__(self):
        return f'-{self.name} : {self.star_type} type star - weighs {self.mass} kg.'


class Moon(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

    def __str__(self):
        return f'-{self.name} : {self.month} days in a month - in orbit around {self.planet.name} - weighs {self.mass} kg.'