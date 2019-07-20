class System():
    bodies = []
    
    def add(self, celestial_body):
        # self.bodies.append(celestial_body)


        # for body in self.bodies:
        if celestial_body not in self.bodies: #Checks if celestial_body is not in the bodies list yet.
            self.bodies.append(celestial_body)


        # body not in self.bodies:
        #     seen.add(body)
        #     item_list.append(body)
            pass

        # return celestial_body



    def total_mass(self):
        total_mass = 0

        for body in self.bodies:
            print(body.mass)
            total_mass += body.mass

        return total_mass







class Body():

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        
    # @classmethod
    # def all(self, system):
    #     print(system.bodies[1].name)





class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

    
    



class Star(Body):
    def __init__(self, name, mass, star_type):
        super().__init__(name, mass)
        self.star_type = star_type

class Moon(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet




solar_system = System()





a_body = Body('A body', 0)
solar_system.add(a_body)


earth = Planet('Earth', 6000000000000000000000000, 24, 365.4)
solar_system.add(earth)


sun = Star('Sun', 2000000000000000000000000000000, 'G-type')
solar_system.add(sun)


moon = Moon('Moon', 73500000000000000000000, '7.35 x 1022 kg', earth)
solar_system.add(moon)
solar_system.add(moon)
solar_system.add(moon)
solar_system.add(moon)
solar_system.add(moon)
solar_system.add(a_body)
solar_system.add(a_body)
solar_system.add(a_body)








print()
print(f'{solar_system.bodies}')

# print(f'{a_body.name} - {a_body.mass}')

# print(f'{earth.name} - {earth.mass} - {earth.day} - {earth.year}')

# print(f'{sun.name} - {sun.mass} - {sun.star_type}')

# print(f'{moon.name} - {moon.mass} - {moon.month} - {moon.planet.name}')

print()

for body in solar_system.bodies:
    print(body.name)



print()

# Planet.all(solar_system)

# Star.all(solar_system)

# Moon.all(solar_system)




alpha_centauri = System()

print()

print(solar_system.total_mass())