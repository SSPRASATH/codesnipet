def dos(): 
	with open('FILE_NAME') as fp:                          # FILE_NAME - enter arff file name
           dosa=[]
	   for line in fp:
		l= line[::-1]
		la=l.split(',',1)
		var=la[0][::-1]
		dos=['back.','neptune.','pod.','smurf.','teardrop.']
	   	for var in dos:
	             f = open('dos.txt', 'a')
	             f.write(line) 
	             f.close()


def u2r(): 
   with open('FILE_NAME') as fp:				# FILE_NAME - enter arff file name
   	u2ra=[]
	print '2'
   	for line in fp:
		l= line[::-1]
		la=l.split(',',1)
		var=la[0][::-1]
		u2r=['buffer_overflow.','loadmodule.','perl.','rootkit.']
	   	for var in u2r:
	             f = open('u2r.txt', 'a')
	             f.write(line) 
	             f.close()
def r2l(): 
   with open('FILE_NAME') as fp:				# FILE_NAME - enter arff file name
   	r2la=[]
   	for line in fp:
		l= line[::-1]
		la=l.split(',',1)
		var=la[0][::-1]
		r2l=['ftp_write.','imap.','multihop.','phf.','spy.','warezclient.','warezmaster.']
	   	for var in r2l:
	             f = open('r2l.txt', 'a')
	             f.write(line) 
	             f.close()

if __name__ == '__main__':
    print '1. dos'
    print '2. u2r'
    print '3. r2l'
    ch = input('enter ur choice >_ ')
    if ch==1:
       dos()
    if ch==2:
       u2r()
    if ch==3:
       r3()
