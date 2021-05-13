#cython: language_level=3
import numpy as np
cimport numpy as cnp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cython

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef evolve(cnp.ndarray[cnp.double_t, ndim=2] u, cnp.ndarray[cnp.double_t, ndim=2] u_previous, double a, double dt, double dx2, double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    cdef int n, m
    n = u.shape[0]
    m = u.shape[1]

    # Multiplication is more efficient than division
    cdef double dx2inv = 1. / dx2
    cdef double dy2inv = 1. / dy2

    cdef int i,j
    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) * dx2inv + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) * dy2inv )
    u_previous[:] = u[:]

@cython.cdivision(True)
def iterate(cnp.ndarray[cnp.double_t, ndim=2] field, cnp.ndarray[cnp.double_t, ndim=2] field0, double a, double dx, double dy, int timesteps, int image_interval):
    """Run fixed number of time steps of heat equation"""

    cdef double dx2, dy2
    dx2 = dx**2
    dy2 = dy**2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    cdef double dt
    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    cdef int m
    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

def init_fields(filename):
    # Read the initial temperature field from file
    field = np.loadtxt(filename)
    field0 = field.copy() # Array for field of previous time step
    return field, field0

cpdef write_field(cnp.ndarray[cnp.double_t, ndim=2] field, int step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))


