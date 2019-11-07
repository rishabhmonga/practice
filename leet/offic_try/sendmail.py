import subprocess
import sys
cmd="""echo "test" | mailx -s 'test!' root"""
p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
output, errors = p.communicate()
print (errors,output)