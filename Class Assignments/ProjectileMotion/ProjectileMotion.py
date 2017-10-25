import matplotlib.pyplot as plt
import math


# Requests input and validates that it is an integer
def integer_input(dialogue):
    while True:
        try:
            return int(input(dialogue))
        except:
            print("Invalid input")


# Main program
def main():
    # Requests how many arcs to make
    graphs = integer_input("How many arcs would you like to graph? ")
    legend = []
    for arcs in range(0, graphs):

        # Requests input for theta
        theta = integer_input("Please input throw angle ")

        # Requests input for initial Velocity
        initial_velocity = integer_input("Please input the initial velocity ")

        # Earth gravitational constant
        gravity = 9.807

        # Time of flight in milliseconds
        time_of_flight = (((2*initial_velocity)*(math.sin(math.radians(theta))))/gravity)*1000

        # Project the vector to find the horizontal and vertical velocities
        velocity_x = (math.cos(math.radians(theta)))*initial_velocity
        velocity_y = (math.sin(math.radians(theta)))*initial_velocity

        # Calculates the x and y coordinates for every millisecond
        x = [velocity_x*(x/1000) for x in range(0, int(time_of_flight))]
        y = [(velocity_y*(x/1000))-((gravity*((x/1000)**2))/2) for x in range(0, int(time_of_flight))]

        # Plots from the x and y lists
        plt.plot(x, y)
        legend.append("arc "+ str(arcs+1))

    # Displays the graph and it's information
    plt.legend(legend)
    plt.title("Projectile Motion")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.show()


main()
