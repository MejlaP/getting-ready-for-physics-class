# Physical properties - values
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Turn up the Temperature
# function converts Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


# test function with a value of 100 Fahrenheit
f100_in_celsius = f_to_c(100)

# function converts Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


# test function with a value of 0 Celsius
c0_in_fahrenheit = c_to_f(0)


# Use the Force
# function for get force
def get_force(mass, acceleration):
    return mass * acceleration


# test function and print result
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

# function for get energy
def get_energy(mass, c=3 * 10 ** 8):
    return mass * c ** 2


# test function and print result
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")


# Do the Work
# function for get work
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance


# test function and print result
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
