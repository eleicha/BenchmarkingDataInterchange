import numpy as np 
import matplotlib as mpl 
import sys
mpl.use('agg')

import matplotlib.pyplot as plt 

def drawTime(size, title):

	protobuf = np.asarray([0.005331765001756139, 0.008730132998607587, 0.0009549469978082925, 0.0010443999999552034, 0.0009671770021668635])
	protobuf_to_disk = []
	capnp = np.asarray([0.005331765001756139, 0.008730132998607587, 0.0009549469978082925, 0.0010443999999552034, 0.0009671770021668635])
	capnp_to_disk =[]
	avro = np.asarray([0.005331765001756139, 0.008730132998607587, 0.0009549469978082925, 0.0010443999999552034, 0.0009671770021668635])
	avro_to_disk =[]


	data_to_plot = [protobuf, protobuf_to_disk, capnp, capnp_to_disk, avro, avro_to_disk]

	fig = plt.figure(1, figsize=(9,6))
	ax = fig.add_subplot(111)
	bp = ax.boxplot(data_to_plot)
	ax.set_ylabel('time in seconds')
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Protobuf to disk', 'Cap\'n Proto', 'Cap\'n Proto to disk', 'Apache Avro', 'Apache Avro to disk',])
	fig.savefig('eval/box_'+str(size), bbox_inches='tight')

def drawCPU(size, title):
	
	protobuf = np.asarray([0.005331765001756139, 0.008730132998607587, 0.0009549469978082925, 0.0010443999999552034, 0.0009671770021668635])
	protobuf_to_disk = []
	capnp = np.asarray([0.005331765001756139, 0.008730132998607587, 0.0009549469978082925, 0.0010443999999552034, 0.0009671770021668635])
	capnp_to_disk =[]
	avro = np.asarray([0.005331765001756139, 0.008730132998607587, 0.0009549469978082925, 0.0010443999999552034, 0.0009671770021668635])
	avro_to_disk =[]

	data_to_plot = [protobuf, protobuf_to_disk, capnp, capnp_to_disk, avro, avro_to_disk]

	fig = plt.figure(1, figsize=(9,6))
	ax = fig.add_subplot(111)
	bp = ax.boxplot(data_to_plot)
	ax.set_ylabel('CPU utilization in %')
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Protobuf to disk', 'Cap\'n Proto', 'Cap\'n Proto to disk', 'Apache Avro', 'Apache Avro to disk',])
	fig.savefig('eval/box_'+str(size), bbox_inches='tight')


def main():

	path = sys.argv[1]

	file = open(str(path), 'r')
	Lines = file.readLines()

	for line in Lines:
		if line.split(':')[0] == 'CPU_UTIL':
			pass
		elif line.split(':')[0] == 'CPU_USER':
		elif line.split(':')[0] == 'CPU_SYSTEM':
		elif line.split(':')[0] == 'CPU_IDLE':
		elif line.split(':')[0] == 'time_stamp':
		elif line.split(':')[0] == 'MEMORY':
		elif line.split(':')[0] == 'TIMES':
		elif line.split(':')[0] == 'read_count':
		elif line.split(':')[0] == 'write_counter':
		elif line.split(':')[0] == 'read_bytes':
		elif line.split(':')[0] == 'write_bytes':
		elif line.split(':')[0] == 'CPU_USER':
		elif line.split(':')[0] == 'CPU_USER':







if __name__ == '__main__':
    main()