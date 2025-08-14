from ftplib import FTP

host = "url"
user = "user"
password = "********"



with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())
    
# =============downloaading from the ftp server======
    with open('test.txt', 'wb') as f:
        ftp.retrbinary("RETR" + "filename", f.write,1024)
        
# =============uploading to the ftp server============
    with open("wordlist.txt", 'rb') as f:
        ftp.storbinary("STOR" + 'upload.txt',f)
        
#================downloading file not in main dir======
    ftp.cwd("dir name")
    with open("file.txt",'wb')as f:
        ftp.retrbinary("RETR" + "otherfile.txt", f.write, 1024)
    ftp.quit()
    


