import edgar
import ftplib
from os import listdir, path
import csv

filenames = []

ftp = ftplib.FTP('ftp.sec.gov')
ftp.login()
for file in listdir('./quarterly_indexes'):
	if file == '.DS_Store': continue
	with open('./quarterly_indexes/' + file) as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for row in reader:
			if (row[2] == '10-K'):
				name = row[1].replace(' ', '_') + '_10-K'
				file = row[4]
				filenames.append((file, name))
				break
	if len(filenames) > 5:
		break

for filename, name in filenames:
	print filename
	localfile = open('./yearly_files/' + name, 'wb')
	try:
	  ftp.retrbinary("RETR " + filename ,localfile.write)
	except Exception as e:
		print e
ftp.close()
	# edgar.download(ftp, file, './quarterly_indexes')
# print csv.list_dialects()
