#!/usr/local/bin/python3
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.122.136',username='jeremy',password='j3r3my',port=22)
ssh.connect(hostname='192.168.122.136',username='jeremy',key_filename='/home/jeremy/.ssh/id_rsa',port=22)
# # stdin, stdout, stderr = ssh.exec_command('whoami')
# stdin, stdout, stderr = ssh.exec_command('uptime')
stdin, stdout, stderr = ssh.exec_command('free -m')
print("The output is: ")
print(stdout.readline())

print("The Error is: ")
print(stderr.readline())


