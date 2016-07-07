import edgar
import ftplib
from os import listdir, path
import csv

quartely_path = path.realpath('./') + '/quarterly_files/'
filenames = []

ftp = ftplib.FTP('ftp.sec.gov')
ftp.login()
for file in listdir('./quarterly_indexes'):
	if file == '.DS_Store': continue
	with open('./quarterly_indexes/' + file) as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			name = row[1].replace(' ', '_')
			file = row[4]
			filenames.append((file, name))
			break
	break

for filename, name in filenames:
	print filename
	localfile = open('./quarterly_files/' + name, 'wb')
	try:
	  ftp.retrbinary("RETR " + filename ,localfile.write)
	except Exception as e:
		print e
	finally:
		ftp.close()
	# edgar.download(ftp, file, './quarterly_indexes')
# print csv.list_dialects()
