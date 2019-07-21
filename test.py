from system import *

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