import numpy as np 
import matplotlib as mpl 
import sys
mpl.use('agg')

import matplotlib.pyplot as plt 

def draw_bar(values, name, title):


	protobuf = np.asarray(values[0])
	capnp = np.asarray(values[1])
	avro = np.asarray(values[2])
	xml = np.asarray(values[3])

	data_to_plot = [protobuf, capnp, avro, xml]

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig = plt.figure(1, figsize=(9,6))
	ax = fig.add_subplot(111)
	bp = ax.barh(data_to_plot)
	ax.set_ylabel(title)
	title = title + ' measured on ' + str(machine)
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/bar_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

def draw_scatter(x, y, name, title, x_label, y_label):
	
	x_protobuf = np.asarray(x[0])
	x_capnp = np.asarray(x[1])
	x_avro = np.asarray(x[2])
	x_xml = np.asarray(x[3])

	y_protobuf = np.asarray(y[0])
	y_capnp = np.asarray(y[1])
	y_avro = np.asarray(y[2])
	y_xml = np.asarray(y[3])

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	plt.scatter(x_protobuf, y_protobuf, color='green')
	plt.scatter(x_capnp, y_capnp, color='blue')
	plt.scatter(x_avro, y_avro, color='red')
	plt.scatter(x_xml, y_xml, color='black')

	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	title = title + ' measured on ' + str(machine)
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/scatter_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

def draw_line_chart(x, y, name, title, x_label, y_label):
	
	x_protobuf = np.asarray(x[0])
	x_capnp = np.asarray(x[1])
	x_avro = np.asarray(x[2])
	x_xml = np.asarray(x[3])

	y_protobuf = np.asarray(y[0])
	y_capnp = np.asarray(y[1])
	y_avro = np.asarray(y[2])
	y_xml = np.asarray(y[3])

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	plt.figure()
	plt.plot(x_protobuf, y_protobuf, color='green')
	plt.plot(x_capnp, y_capnp, color='blue')
	plt.plot(x_avro, y_avro, color='red')
	plt.plot(x_xml, y_xml, color='black')

	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	title = title + ' measured on ' + str(machine)
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/line_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

def draw_boxplot(values, name, title):
	
	protobuf = np.asarray(values[0])
	capnp = np.asarray(values[1])
	avro = np.asarray(values[2])
	xml = np.asarray(values[3])

	data_to_plot = [protobuf, capnp, avro, xml]

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig = plt.figure(1, figsize=(9,6))
	ax = fig.add_subplot(111)
	bp = ax.boxplot(data_to_plot)
	ax.set_ylabel(title)
	title = title + ' measured on ' + str(machine)
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/box_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')


def main():

	cpu_util = []
	cpu_user = []
	cpu_system = []
	cpu_idle = []
	time_stamp = []
	memory = []
	times = []
	read_count = []
	write_counter = []
	read_bytes = []
	write_bytes = []
	read_time = []
	write_time = []
	bytes_recv = []
	packets_recv = []
	write_time = []
	bytes_sent = []
	packets_sent = []

	paths = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]

	for path in paths:
		pass

		file = open(str(path), 'r')
		Lines = file.readLines()

		for line in Lines:
			if line.split(':')[0] == 'CPU_UTIL':
				cpu_util.append(line.split(':')[1])
			elif line.split(':')[0] == 'CPU_USER':
				cpu_user.append(line.split(':')[1])
			elif line.split(':')[0] == 'CPU_SYSTEM':
				cpu_system.append(line.split(':')[1])
			elif line.split(':')[0] == 'CPU_IDLE':
				cpu_idle.append(line.split(':')[1])
			elif line.split(':')[0] == 'time_stamp':
				time_stamp.append(line.split(':')[1])
			elif line.split(':')[0] == 'MEMORY':
				memory.append(line.split(':')[1])
			elif line.split(':')[0] == 'TIMES':
				times.append(line.split(':')[1])
			elif line.split(':')[0] == 'read_count':
				read_count.append(line.split(':')[1])
			elif line.split(':')[0] == 'write_counter':
				write_counter.append(line.split(':')[1])
			elif line.split(':')[0] == 'read_bytes':
				read_bytes.append(line.split(':')[1])
			elif line.split(':')[0] == 'write_bytes':
				write_bytes.append(line.split(':')[1])
			elif line.split(':')[0] == 'read_time':
				read_time.append(line.split(':')[1])
			elif line.split(':')[0] == 'write_time':
				write_time.append(line.split(':')[1])
			elif line.split(':')[0] == 'bytes_recv':
				bytes_recv.append(line.split(':')[1])
			elif line.split(':')[0] == 'packets_recv':
				packets_recv.append(line.split(':')[1])
			elif line.split(':')[0] == 'bytes_sent':
				bytes_sent.append(line.split(':')[1])
			elif line.split(':')[0] == 'packets_sent':
				packets_sent.append(line.split(':')[1])


	draw_boxplot(times, paths[0].split('/')[1], 'Time')
	draw_scatter(bytes_recv, cpu_util, paths[0].split('/')[1], 'CPU Utilization', 'Bytes Received', 'CPU Utilization in %')
	draw_scatter(bytes_recv, memory, paths[0].split('/')[1], 'Memory Utilization', 'Bytes Received', 'Memory Utilization in %')
	draw_boxplot(bytes_sent, paths[0].split('/')[1], 'Bytes Sent')
	draw_boxplot(bytes_recv, paths[0].split('/')[1], 'Bytes Received')
	draw_scatter(write_time, bytes_recv, paths[0].split('/')[1], 'Bytes Written', 'Time to Write to disk in ms', 'Data Received in Bytes')
	draw_scatter(write_time, write_bytes, paths[0].split('/')[1], 'Bytes Written', 'Time to Write to disk in ms', 'Data Written in Bytes')
	draw_scatter(read_time, read_bytes, paths[0].split('/')[1], 'Bytes Read', 'Time to Read data in ms', 'Data Read in Bytes')
	draw_scatter(read_time, bytes_recv, paths[0].split('/')[1], 'Bytes Read', 'Time to Write to disk in ms', 'Data Received in Bytes')



if __name__ == '__main__':
    main()