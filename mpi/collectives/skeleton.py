from mpi4py import MPI
import numpy

# mpirun -np 4 python3 skeleton.py
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('Broadcast:')

# Simple broadcast
if rank == 0:
    data = numpy.arange(8)
else:
    data = numpy.empty(8, int)
comm.Bcast(data, root=0)
print('  Task {0}: {1}'.format(rank, data))


# Prepare data vectors ..
data = numpy.arange(8)
data += rank * 8
# .. and receive buffers
buff = numpy.zeros(8, int)
buff[:] = -1

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Data vectors:')
print('  Task {0}: {1}'.format(rank, data))
comm.barrier()
if rank == 0:
    print('')
    print('Scatter:')

# Scatter one vector
comm.Scatter(data, buff[:2], root=0)
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('Gather:')

# Gather equal amount of data from each MPI task
comm.Gather(data[:2], buff, root=1)
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('Reduce:')

# Calculate partial sums using two communicators
color = rank // 2
sub_comm = comm.Split(color)
sub_comm.Reduce(data, buff, op=MPI.SUM, root=0)
print('  Task {0}: {1}'.format(rank, buff))
