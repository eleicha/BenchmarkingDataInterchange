import numpy as np 
import matplotlib as mpl 
import sys
mpl.use('agg')

import matplotlib.pyplot as plt 
'''
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
	if int(print_to_file) == 1:
		title = title + ' (Data Written to Disk)'
	ax.set_title(str(title))
	ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/bar_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')
'''
def draw_scatter_message_length(x1, x2, x3, x4, y, name, title, x_label, y_label):

	x_protobuf = np.asarray(x1)
	x_capnp = np.asarray(x2)
	x_avro = np.asarray(x3)
	x_xml = np.asarray(x4)

	y_protobuf = np.asarray(y[0])
	y_capnp = np.asarray(y[1])
	y_avro = np.asarray(y[2])
	y_xml = np.asarray(y[3])

	#print(x_xml)

	#print('len prot ', len(x_protobuf), 'len y ', len(y_protobuf))
	#print('len xml ', len(x_xml), 'len y ', len(y_xml))

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig1, ax1 = plt.subplots()

	proto = ax1.scatter(x_protobuf, y_protobuf, c='g')
	capnp = ax1.scatter(x_capnp, y_capnp, color='b')
	avro = ax1.scatter(x_avro, y_avro, color='r')
	xml = ax1.scatter(x_xml, y_xml, color='k')

	#plt.legend((y_protobuf, y_capnp, y_avro, y_xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'), scatterpoints=1)

	ax1.set_ylabel(y_label)
	ax1.set_xlabel(x_label)
	ax1.legend((proto, capnp, avro, xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'))
	title = title + ' Measured on ' + str(machine).capitalize()
	if int(print_to_file) == 1:
		title = title + ' (Data Written to Disk)'
	ax1.set_title(str(title))
	#plt.xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])

	fig1.savefig('eval/scatter_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

def draw_scatter(x, scale_x, y, scale_y, name, title, x_label, y_label):
	
	x_protobuf = np.asarray(x[0])-scale_x[0]
	x_capnp = np.asarray(x[1])-scale_x[1]
	x_avro = np.asarray(x[2])-scale_x[1]
	x_xml = np.asarray(x[3])-scale_x[1]

	y_protobuf = np.asarray(y[0])-scale_y[0]
	y_capnp = np.asarray(y[1])-scale_y[1]
	y_avro = np.asarray(y[2])-scale_y[2]
	y_xml = np.asarray(y[3])-scale_y[3]

	#print('len prot ', len(x_protobuf), 'len y ', len(y_protobuf))

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig2, ax2 = plt.subplots()

	proto = ax2.scatter(x_protobuf, y_protobuf, c='g')
	capnp = ax2.scatter(x_capnp, y_capnp, color='b')
	avro = ax2.scatter(x_avro, y_avro, color='r')
	xml = ax2.scatter(x_xml, y_xml, color='k')

	#plt.legend((y_protobuf, y_capnp, y_avro, y_xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'), scatterpoints=1)

	ax2.set_ylabel(y_label)
	ax2.set_xlabel(x_label)
	ax2.legend((proto, capnp, avro, xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'))
	title = title + ' Measured on ' + str(machine).capitalize()
	if int(print_to_file) == 1:
		title = title + ' (Data Written to Disk)'
	ax2.set_title(str(title))
	#plt.xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])

	fig2.savefig('eval/scatter_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

def draw_scatter_disk(x, start_value_x, y, start_value_y, name, title, x_label, y_label):
	
	x_protobuf = np.asarray(x[0])-start_value_x[0]
	x_capnp = np.asarray(x[1])-start_value_x[1]
	x_avro = np.asarray(x[2])-start_value_x[2]
	x_xml = np.asarray(x[3])-start_value_x[3]

	y_protobuf = np.asarray(y[0])-start_value_y[0]
	y_capnp = np.asarray(y[1])-start_value_y[1]
	y_avro = np.asarray(y[2])-start_value_y[2]
	y_xml = np.asarray(y[3])-start_value_y[3]

	#print('len prot ', len(x_protobuf), 'len y ', len(y_protobuf))
	#print('len prot ', len(x_xml), 'len y ', len(y_xml))
	#print(y_xml)
	#print(x_xml)

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig3, ax3 = plt.subplots()

	proto = ax3.scatter(x_protobuf, y_protobuf, c='g')
	capnp = ax3.scatter(x_capnp, y_capnp, color='b')
	avro = ax3.scatter(x_avro, y_avro, color='r')
	xml = ax3.scatter(x_xml, y_xml, color='k')

	#plt.legend((y_protobuf, y_capnp, y_avro, y_xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'), scatterpoints=1)

	ax3.set_ylabel(y_label)
	ax3.set_xlabel(x_label)
	ax3.legend((proto, capnp, avro, xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'))
	title = title + ' Measured on ' + str(machine).capitalize()
	if int(print_to_file) == 1:
		filetitle = title +'_disk'
		#title = title + ' (Data Written to Disk)'
	ax3.set_title(str(title))
	#plt.xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])

	fig3.savefig('eval/scatter_'+str(filetitle)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file)+'.png', bbox_inches='tight')

def draw_scatter_mul_y(x,discount, y1, y2, y3, y4, name, title, x_label, y_label):
	
	x_protobuf = np.asarray(x[0])-discount[0]
	x_capnp = np.asarray(x[1])-discount[1]
	x_avro = np.asarray(x[2])-discount[2]
	x_xml = np.asarray(x[3])-discount[3]

	y_protobuf = np.asarray(y1)
	y_capnp = np.asarray(y2)
	y_avro = np.asarray(y3)
	y_xml = np.asarray(y4)

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig4, ax4 = plt.subplots()

	proto = ax4.scatter(x_protobuf, y_protobuf, c='g')
	capnp = ax4.scatter(x_capnp, y_capnp, color='b')
	avro = ax4.scatter(x_avro, y_avro, color='r')
	xml = ax4.scatter(x_xml, y_xml, color='k')

	#plt.legend((y_protobuf, y_capnp, y_avro, y_xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'), scatterpoints=1)

	ax4.set_ylabel(y_label)
	ax4.set_xlabel(x_label)
	ax4.legend((proto, capnp, avro, xml), ('Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'))
	title = title + ' Measured on ' + str(machine).capitalize()
	#if int(print_to_file) == 1:
		#title = title + ' (Data Written to Disk)'
	ax4.set_title(str(title))
	#plt.xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])

	fig4.savefig('eval/scatter_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')

'''
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
	if int(print_to_file) == 1:
		title = title + ' (data written to disk)'
	ax.set_title(str(title))
	#ax.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig.savefig('eval/line_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')
'''
def draw_boxplot_xml(values, start_value_bytes_rec, name, title):

	#print(values)
	data_to_plot = []
	val = []
	for i in range(0, len(values)):
		val.append(values[i])
		print(values[i])
		if (i + 1)%10 == 0 :
			print(val)
			data_to_plot.append(val)
			val = []
	'''
	protobuf = np.asarray(values[0])-start_value_bytes_rec[0]
	capnp = np.asarray(values[1])-start_value_bytes_rec[0]
	avro = np.asarray(values[2])-start_value_bytes_rec[0]
	xml = np.asarray(values[3])-start_value_bytes_rec[0]

	data_to_plot = [protobuf, capnp, avro, xml]
	'''
	print(data_to_plot)
	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig5, ax5 = plt.subplots()

	#ax = fig.add_subplot(111)
	ax5.boxplot(data_to_plot)
	ax5.set_ylabel('Size of Received Message in Bytes')
	ax5.set_xlabel('Size of Sent Message in Bytes')
	title = title + ' Measured on ' + str(machine).capitalize()
	if print_to_file == 1:
		title = title + ' (data written to disk)'
	ax5.set_title(str(title))
	ax5.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
	ax5.set_xticklabels(['224', '410', '596', '782', '968','1154','1340','1526','1712','1898','2084','2270','2456','2642','2828','3014','3200','3386','3572','3758','3944','4130','4316','4502','4688'])
	ax5.tick_params(axis='x',rotation=45)
	fig5.savefig('eval/box_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')


def draw_boxplot(values, start_value_bytes_rec, name, title):

	print(values)

	
	protobuf = np.asarray(values[0])-start_value_bytes_rec[0]
	capnp = np.asarray(values[1])-start_value_bytes_rec[0]
	avro = np.asarray(values[2])-start_value_bytes_rec[0]
	xml = np.asarray(values[3])-start_value_bytes_rec[0]

	data_to_plot = [protobuf, capnp, avro, xml]

	machine = name.split('_')[0]
	number_of_people = name.split('_')[2]
	number_of_messages = name.split('_')[3]
	print_to_file = name.split('_')[4]

	fig6, ax6 = plt.subplots()

	#ax = fig.add_subplot(111)
	ax6.boxplot(data_to_plot)
	ax6.set_ylabel(title)
	title = title + ' Measured on ' + str(machine).capitalize()
	if int(print_to_file) == 1:
		title = title + ' (data written to disk)'
	ax6.set_title(str(title))
	ax6.set_xticks([1,2,3,4])
	ax6.set_xticklabels(['Protobuf', 'Cap\'n Proto', 'Apache Avro', 'XML'])
	fig6.savefig('eval/box_'+str(title)+'_'+str(machine)+'_'+str(number_of_people)+'_'+str(number_of_messages)+'_'+str(print_to_file), bbox_inches='tight')


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
	message_length_proto = []
	message_length_capnp = []
	message_length_avro = []
	message_length_xml = []
	start_value_disk = []
	start_value_bytes_rec = []
	start_value_bytes_sent = []

	paths = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]

	for path in paths:
		identify_format = path.split('/')[1].split('_')[1]
		#print(identify_format)

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
						#print(value)
				bytes_sent.append(values)
			elif line.split(':')[0] == 'packets_sent':
				values = []
				for value in line.split(':')[1].lstrip('[').rstrip(']').split(','):
					if len(value) != 0:
						values.append(float(value))
				packets_sent.append(values)
			elif line.split(':')[0] == 'start_value_disk':
				start_value_disk.append(float(line.split(':')[1]))
				#print(start_value_disk)
			elif line.split(':')[0] == 'start_value_bytes_rec':
				start_value_bytes_rec.append(float(line.split(':')[1]))
				#print(start_value_bytes_rec)
			elif line.split(':')[0] == 'start_value_bytes_sent':
				start_value_bytes_sent.append(float(line.split(':')[1]))
				#print(start_value_bytes_rec)
			elif line.split(':')[0] == 'message_length':
				message_length_one_ex = []
				l = line.split(':')[1].lstrip('[').rstrip(']').split(']')[0]
				if len(l) != 0:
					for value in l.split(','):
						if len(value) != 0:
							#print(len(value))
							message_length_one_ex.append(float(value.lstrip(' [')))
				if int(identify_format) == 0:
					message_length_proto = message_length_one_ex
				elif int(identify_format) == 1:
					message_length_capnp = message_length_one_ex
				elif int(identify_format) == 2:
					message_length_avro = message_length_one_ex
				elif int(identify_format) == 3:
					message_length_xml = message_length_one_ex
				

	machine = paths[0].split('/')[1].split('_')[0]
	print_to_file = paths[0].split('/')[1].split('_')[4]
	#print(message_length_proto)

	if machine == 'server':
		

		draw_scatter_message_length(message_length_proto, message_length_capnp, message_length_avro, message_length_xml, cpu_util, paths[0].split('/')[1], 'CPU Utilization', 'Message Size in Bytes', 'CPU Utilization in %')
		draw_scatter_message_length(message_length_proto, message_length_capnp, message_length_avro, message_length_xml, memory, paths[0].split('/')[1], 'Memory Utilization', 'Message Size in Bytes', 'Memory Utilization in %')

		if int(print_to_file) == 1:
			draw_scatter_disk(write_time, [write_time[0][0],write_time[1][0],write_time[2][0],write_time[3][0]], write_bytes, start_value_disk, paths[0].split('/')[1], 'Bytes Written', 'Time to Write to Disk in ms', 'Data Written in Bytes')
			draw_scatter_disk(write_bytes, start_value_disk, bytes_recv, start_value_bytes_rec, paths[0].split('/')[1], 'Data Received vs. Data Writtento Disk', 'Data Written to Disk in Bytes', 'Data Received in Bytes')
			draw_scatter_disk(write_time, [write_time[0][0],write_time[1][0],write_time[2][0],write_time[3][0]], bytes_recv, start_value_bytes_rec, paths[0].split('/')[1], 'Time to Write Received Bytes', 'Time to Write Bytes in ms', 'Bytes Received')
			draw_scatter_mul_y(write_time, [write_time[0][0],write_time[1][0],write_time[2][0],write_time[3][0]], message_length_proto, message_length_capnp, message_length_avro, message_length_xml, paths[0].split('/')[1], 'Time to Write Message', 'Time to Write Message in ms', 'Message Size in Bytes')

			#draw_scatter(read_time, read_bytes, paths[0].split('/')[1], 'Bytes Read', 'Time to Read data in ms', 'Data Read in Bytes')
			#draw_scatter(read_time, bytes_recv, paths[0].split('/')[1], 'Bytes Read', 'Time to Write to disk in ms', 'Data Received in Bytes')

		draw_scatter(read_time, [0,0,0,0], bytes_recv, start_value_bytes_rec, paths[0].split('/')[1], 'Time to Read Bytes', 'Time to Read Bytes in ms', 'Bytes Received')
		draw_scatter_mul_y(read_time, [0,0,0,0], message_length_proto, message_length_capnp, message_length_avro, message_length_xml, paths[0].split('/')[1], 'Time to Read Message', 'Time to Read Message in ms', 'Message Size in Bytes')


		draw_boxplot_xml(message_length_xml, start_value_bytes_rec, paths[0].split('/')[1], 'Deviations in Message Sizes')
		#draw_boxplot(bytes_recv, start_value_bytes_rec, paths[0].split('/')[1], 'Bytes Received')
		draw_boxplot(times, [0,0,0,0], paths[0].split('/')[1], 'Processing Time')

	elif machine == 'client':
		#draw_boxplot(times,[0,0,0,0], paths[0].split('/')[1], 'Processing Time')
		draw_boxplot(bytes_sent, start_value_bytes_sent, paths[0].split('/')[1], 'Bytes Sent')
		draw_scatter_message_length(message_length_proto, message_length_capnp, message_length_avro, message_length_xml, cpu_util, paths[0].split('/')[1], 'CPU Utilization', 'Message Size in Bytes', 'CPU Utilization in %')
		draw_scatter_message_length(message_length_proto, message_length_capnp, message_length_avro, message_length_xml, memory, paths[0].split('/')[1], 'Memory Utilization', 'Message Size in Bytes', 'Memory Utilization in %')




if __name__ == '__main__':
    main()