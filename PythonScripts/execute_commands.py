
import subprocess
# cmd="ls -lrt"
# cmd=['echo','$HOME']
cmd='echo $HOME'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
print(f'The output :\n{out.splitlines()}')
print(f'The error :\n{err.splitlines()}')
# cmd=['ls','-lrt']
# cmd=['echo','$HOME']
# sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# rc=sp.wait()
# out,err=sp.communicate()

# print(f'The return code: {rc}')
# print(f'The output :\n{out.splitlines()}')
# print(f'The error :\n{err.splitlines()}')

