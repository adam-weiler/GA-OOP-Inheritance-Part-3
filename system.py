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

        # print(cls.all_bodies)
        for body in cls.all_bodies:
            # print(body.name)
            total_mass += body.mass

        # for body in self.bodies:
            # print(body.name)
            # total_mass += body.mass

        return total_mass


class Body():
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        
    # @classmethod
    # def all(self, system):
    #     print(system.bodies[1].name)

    @classmethod
    def list_all(self, body_type):
        for body in System.bodies: #Iterates through each body in System.bodies list.
            if isinstance(body, body_type): #If current body is of body_type. ie: Planet.
                print(body) #Prints the class-specific __str__ method.

            # print(isinstance(body, body_type)) 





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



solar_system = System('Solar')
print(solar_system)

mercury = Planet('Mercury', 3.285 * 10**23, 1408, 87.969)
print(solar_system.add(mercury))
print()

venus = Planet('Venus', 4.867 * 10**24, 5832, 224.7)
print(solar_system.add(venus))
print()

earth = Planet('Earth', 5.972 * 10**24, 24, 365.2564)
print(solar_system.add(earth))
print()

mars = Planet('Mars', 6.39 * 10**23, 25, 687)
print(solar_system.add(mars))
print(solar_system.add(mars)) #It won't let you add the same celestial body more than once.
print(solar_system.add(mars))
print()

jupiter = Planet('Jupiter', 1.898 * 10 ** 27, 10, 4332.59)
print(solar_system.add(jupiter))
print()

sun = Star('Sun', 1.989 * 10**30, 'G-type')
print(solar_system.add(sun))
print()

moon = Moon('Moon', 7.35 * 10**22, 27, earth)
print(solar_system.add(moon))
print()

europa = Moon('Europa', 4.7998 * 10 ** 22, 3.5, jupiter)
print(solar_system.add(europa))
print()

print('A list of Planets:')
solar_system.list_all(Planet)
print()

print('A list of Stars:')
solar_system.list_all(Star)
print()

print('A list of Moons:')
solar_system.list_all(Moon)
print('\n\n')



alpha_centauri = System('Alpha Centauri')
print(alpha_centauri)

proxima_centauri_b = Planet('Proxima Centauri b', 3.285 * 10**23, 180, 11.186)
print(alpha_centauri.add(proxima_centauri_b))
print()

proxima_centauri = Star('Proxima Centauri', 2.446 * 10**29, 'M-type')
print(alpha_centauri.add(proxima_centauri))
print()

print('A list of Planets:')
alpha_centauri.list_all(Planet)
print()

print('A list of Stars:')
alpha_centauri.list_all(Star)
print()

print('A list of Moons:')
alpha_centauri.list_all(Moon)
print('\n')

print(f'Total mass of all systems: {System.total_mass()} kg')