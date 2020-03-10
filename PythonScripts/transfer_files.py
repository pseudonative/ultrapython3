#!/usr/local/bin/python3
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.122.136',username='jeremy',key_filename='/home/jeremy/.ssh/id_rsa',port=22)
sftp_client=ssh.open_sftp()

# sftp_client.get('/home/jeremy/paramiko_download.txt','paramiko_downloaded_file.txt')
# sftp_client.chdir("/home/jeremy")
# print(sftp_client.getcwd())
# sftp_client.get('demoFromPyClone.txt','/home/jeremy/From_PY_Clone/DownLoaded_demoFromPyClone.txt')
sftp_client.put("transfer_files.py",'/home/jeremy/transfer_files.py')
sftp_client.close()
ssh.close()





