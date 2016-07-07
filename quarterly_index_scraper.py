import edgar
import ftplib
ftp = ftplib.FTP(edgar.FTP_ADDR)
ftp.login()
print dir(edgar)
try:
	for file in edgar.downloader.quarterly_file_list(1993):
		edgar.download(ftp, file, './quarterly_indexes')
except Exception as e:
	print e
	ftp.close()
finally:
	ftp.close()