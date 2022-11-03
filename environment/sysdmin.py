#task 1 - list contents of dir from os module
import os
os.system("ls")

#task2 - list contents of dir from subprocesses module
#subprocesses run with one argument
import subprocess
subprocess.run(["ls"])

#task3 - list contents and permission of files from subprocesses module
#subprocesses run with two arguments
subprocess.run(["ls", "-l"])

#task4 - show file permission 
#subprocesses with three arguments
subprocess.run(["ls", "-l", "README.md"])

#task5 - retrieving system info ... runnning bash commmands
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#task6 - retrieving disk info 
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
