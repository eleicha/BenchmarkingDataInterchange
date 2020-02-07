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
	title = title + ' Measured on ' + str(machine).capitalize()
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

	print('len prot ', len(x_protobuf), 'len y ', len(y_protobuf))

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	plt.scatter(x_protobuf, y_protobuf, c='g')
	plt.scatter(x_capnp, y_capnp, color='b')
	plt.scatter(x_avro, y_avro, color='r')
	plt.scatter(x_xml, y_xml, color='k')

	#plt.legend((y_protobuf, y_capnp, y_avro, y_xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'), scatterpoints=1)

	plt.ylabel(y_label)
	plt.xlabel(x_label)
	title = title + ' Measured on ' + str(machine).capitalize()
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	plt.title(str(title))
	#plt.xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])

	plt.savefig('eval/scatter_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

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
	title = title + ' Measured on ' + str(machine).capitalize()
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	ax.set_title(str(title))
	#ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/line_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

def draw_boxplot(values, name, title):

	#print(values)

	
	protobuf = np.asarray(values[0])
	capnp = np.asarray(values[1])
	avro = np.asarray(values[2])
	xml = np.asarray(values[3])

	data_to_plot = [protobuf, capnp, avro, xml]

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	plt.figure()
	#ax = fig.add_subplot(111)
	plt.boxplot(data_to_plot)
	plt.ylabel(title)
	title = title + ' Measured on ' + str(machine).capitalize()
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	plt.title(str(title))
	plt.xticks([1,2,3,4],['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	plt.savefig('eval/box_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')


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

		with open(str(path), 'r') as f:
			Lines = [line.rstrip('\n') for line in f]

		for line in Lines:
			if line.split(':')[0] == 'CPU_UTIL':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				cpu_util.append(values)
			elif line.split(':')[0] == 'CPU_USER':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				cpu_user.append(values)
			elif line.split(':')[0] == 'CPU_SYSTEM':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				cpu_system.append(values)
			elif line.split(':')[0] == 'CPU_IDLE':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				cpu_idle.append(values)
			elif line.split(':')[0] == 'time_stamp':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				time_stamp.append(values)
			elif line.split(':')[0] == 'MEMORY':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				memory.append(values)
			elif line.split(':')[0] == 'TIMES':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				times.append(values)
			elif line.split(':')[0] == 'read_count':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				read_count.append(values)
			elif line.split(':')[0] == 'write_counter':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				write_counter.append(values)
			elif line.split(':')[0] == 'read_bytes':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:	
						values.append(float(value))
				read_bytes.append(values)
			elif line.split(':')[0] == 'write_bytes':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:	
						values.append(float(value))
				write_bytes.append(values)
			elif line.split(':')[0] == 'read_time':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				read_time.append(values)
			elif line.split(':')[0] == 'write_time':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				write_time.append(values)
			elif line.split(':')[0] == 'bytes_recv':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				bytes_recv.append(values)
			elif line.split(':')[0] == 'packets_recv':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				packets_recv.append(values)
			elif line.split(':')[0] == 'bytes_sent':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
						print(value)
				bytes_sent.append(values)
			elif line.split(':')[0] == 'packets_sent':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				packets_sent.append(values)


	machine = paths[0].split('/')[1].split('_')[0]
	print_to_file = paths[0].split('/')[1].split('_')[4]


	if machine == 'server':
		if print_to_file == 1:
			draw_scatter(write_time, write_bytes, paths[0].split('/')[1], 'Bytes Written', 'Time to Write to disk in ms', 'Data Written in Bytes')
			draw_scatter(write_time, bytes_recv, paths[0].split('/')[1], 'Bytes Written', 'Time to Write to disk in ms', 'Data Received in Bytes')
			draw_scatter(read_time, read_bytes, paths[0].split('/')[1], 'Bytes Read', 'Time to Read data in ms', 'Data Read in Bytes')
			draw_scatter(read_time, bytes_recv, paths[0].split('/')[1], 'Bytes Read', 'Time to Write to disk in ms', 'Data Received in Bytes')

		draw_scatter(bytes_recv, cpu_util, paths[0].split('/')[1], 'CPU Utilization', 'Bytes Received', 'CPU Utilization in %')
		draw_scatter(bytes_recv, memory, paths[0].split('/')[1], 'Memory Utilization', 'Bytes Received', 'Memory Utilization in %')
		draw_boxplot(bytes_recv, paths[0].split('/')[1], 'Bytes Received')
		draw_boxplot(times, paths[0].split('/')[1], 'Processing Time')


	elif machine == 'client':
		draw_boxplot(times, paths[0].split('/')[1], 'Processing Time')
		draw_boxplot(bytes_sent, paths[0].split('/')[1], 'Bytes Sent')


if __name__ == '__main__':
    main()