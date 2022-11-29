from ftplib import FTP

if __name__ == '__main__':
    # HOST = "172.16.41.108"
    HOST = "172.16.51.121"
    # 172.16.41.108 - ВКМ-1
    # 172.16.51.121 - Депо
    USER = "uploadhis"
    PASSWORD = "111111"
    WORKDIR = "usbdisk/disk_a_1/screenshots/"
    with FTP(HOST) as ftp:
        ftp.login(user=USER, passwd=PASSWORD)
        ftp.cwd(WORKDIR)
        ftp.dir()
