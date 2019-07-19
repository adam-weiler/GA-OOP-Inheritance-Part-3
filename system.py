class System():
    bodies = []
    
    def add(self, celestial_body):
        self.bodies.append(celestial_body)
        return celestial_body

    def total_mass(self):
        return sum(self.bodies)



class Body():

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        

class Planet(Body):
    def __init__(self, name, mass, day, year):
        self.name = name
        self.mass = mass
        self.day = day
        self.year = year

class Star(Body):
    def __init__(self, name, mass, star_type):
        self.name = name
        self.mass = mass
        self.star_type = star_type

class Moon(Body):
    def __init__(self, name, mass, month, planet):
        self.name = name
        self.mass = mass
        self.month = month
        self.planet = planet




solar_system = System()



something = Body('Something', 100)


earth = Planet('Earth', 42, 24, 365.4)


sun = Star('Sun', '1.989 × 10^30 kg', 'G-type')


moon = Moon('Moon', 27, '7.35 x 1022 kg', earth)


print(solar_system.bodies)

print(f'{something.name} - {something.mass}')

print(f'{earth.name} - {earth.mass} - {earth.day} - {earth.year}')

print(f'{sun.name} - {sun.mass} - {sun.star_type}')

print(f'{moon.name} - {moon.mass} - {moon.month} - {moon.planet.name}')