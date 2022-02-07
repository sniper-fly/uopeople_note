import math

# I used math library to express pi constant.
# Plus, I used pow function to calclate r cubed.
def print_volume(r):
    print(math.pi * 4 * pow(r, 3) / 3)

print_volume(3)
# output --> 113.09733552923255

print_volume(10)
# output --> 4188.790204786391

print_volume(1)
# output --> 4.1887902047863905
