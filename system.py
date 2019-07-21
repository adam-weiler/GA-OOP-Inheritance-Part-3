class System():
    bodies = []
    
    def add(self, celestial_body):
        if celestial_body not in self.bodies: #Checks if celestial_body is not in the bodies list yet.
            self.bodies.append(celestial_body)
            return f'Adding {celestial_body.name} to the system.\n'
        else:
            return f'You can\'t add {celestial_body.name} again.\n'


    def total_mass(self):
        total_mass = 0

        for body in self.bodies:
            # print(body.mass)
            total_mass += body.mass

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

    # @classmethod
    # def list_all(self):
    #     for body in System.bodies:
    #         # print(type(body))
    #         print(body.name)
    #         print(isinstance(body, self))

    #         # print(inspect.isclass(Planet))
            

    #         # isinstance()
    #         # if inspect.isclass(Planet) == True:
    #         #     print('yes')
    #         # else:
    #         #     print('no')
    #         pass
    #     # print(System.bodies[1].name)

        

class Star(Body):
    def __init__(self, name, mass, star_type):
        super().__init__(name, mass)
        self.star_type = star_type

    def __str__(self):
        return f'-{self.name} : {self.star_type} type star - weighs {self.mass} kg.'

    # @classmethod
    # def list_all(self):
    #     for body in System.bodies:
    #         print(body.name)
    #         print(isinstance(body, self))

class Moon(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

    def __str__(self):
        return f'-{self.name} : {self.month} days in a month - rotates around planet {self.planet.name} - weighs {self.mass} kg.'

    # @classmethod
    # def list_all(self):
    #     for body in System.bodies:
    #         print(body.name)
    #         print(isinstance(body, self))




solar_system = System()

# a_body = Body('A body', 0)
# solar_system.add(a_body)

mercury = Planet('Mercury', 3.285 * 10**23, 1408, 87.969)
# solar_system.add(mercury)
print(solar_system.add(mercury))

venus = Planet('Venus', 4.867 * 10**24, 5832, 224.7)
# solar_system.add(venus)
print(solar_system.add(venus))

earth = Planet('Earth', 5.972 * 10**24, 24, 365.2564)
print(solar_system.add(earth))

mars = Planet('Mars', 6.39 * 10**23, 25, 687)
print(solar_system.add(mars))
print(solar_system.add(mars)) #It won't let you add the same celestial body more than once.

sun = Star('Sun', 1.989 * 10**30, 'G-type')
print(solar_system.add(sun))

moon = Moon('Moon', 7.35 * 10**22, 27, earth)
print(solar_system.add(moon))



# Planet.list_all()
# print()
# Star.list_all()
# print()
# Moon.list_all()



print('A list of Planets:')
Body.list_all(Planet)
print('\nA list of Stars:')
Body.list_all(Star)
print('\nA list of Moons:')
Body.list_all(Moon)



# solar_system.add(a_body)
# solar_system.add(a_body)
# solar_system.add(a_body)








# print()
# print(f'{solar_system.bodies}')

# print(f'{a_body.name} - {a_body.mass}')

# print(f'{earth.name} - {earth.mass} - {earth.day} - {earth.year}')

# print(f'{sun.name} - {sun.mass} - {sun.star_type}')

# print(f'{moon.name} - {moon.mass} - {moon.month} - {moon.planet.name}')

# print()

# for body in solar_system.bodies:
#     print(body.name)



print()

# Planet.all(solar_system)

# Star.all(solar_system)

# Moon.all(solar_system)




alpha_centauri = System()

print()

print(f'Total mass: {solar_system.total_mass()} kg')