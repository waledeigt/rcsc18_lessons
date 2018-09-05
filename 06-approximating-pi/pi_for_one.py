import numpy as np
import matplotlib.pyplot as plt

#%matplotlib notebook


def circle_bound(x):
    y = np.sqrt(1 - x**2)
    #print(y)
    return y

def lets_make_pi(tot_points):
    circ_points = 0

    for i in range(tot_points):

        point_x = np.random.uniform(0,1)
        point_y = np.random.uniform(0,1)

        if circle_bound(point_x) >= point_y:
            circ_points = circ_points + 1
            plt.scatter(point_x, point_y,c="r")
        else:
            plt.scatter(point_x, point_y,c="b")
            
    pi = 4 * circ_points/tot_points
    #plt.axis("square")
    plt.title(f"Approximating Pi, Monte Carlo Approx. pi $\sim$ {pi}" )
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.show()
    return pi
