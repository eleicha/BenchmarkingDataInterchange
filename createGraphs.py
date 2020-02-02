import numpy as np 
import matplotlib as mpl 
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
	ax.set_ylabel('CPU utilization in %')
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Protobuf to disk', 'Cap\'n Proto', 'Cap\'n Proto to disk', 'Apache Avro', 'Apache Avro to disk',])
	fig.savefig('eval/box_'+str(size), bbox_inches='tight')


def main():
size = input("How large was the transferred data? ")
title = input("What should be the title? ")





if __name__ == '__main__':
    main()