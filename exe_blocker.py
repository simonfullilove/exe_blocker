import os
# shell required to run os commands as admin
import win32com.shell.shell as shell

runfileyn = 'x'
while runfileyn != '':
	path = input('Enter a directory path in which to block executable files: ')

	# crawls path directory and creates array of executables found in it and subdirectories
	exes = []
	for folder in os.walk(path):
		for found_file in folder[2]:
			if found_file[-4:].lower() == '.exe':
				exes.append(folder[0] + '\\' + found_file)

	# if any exes found, creates a one line cmd command creating rule for each exe
	if len(exes) > 0:
		command = ''
		for exe in exes:
			print('Executable found:', exe)
			if command != '':
				command += '&&'
			command += 'netsh advfirewall firewall add rule name="BlockProgram" dir=out program="' + exe + '" profile=any action=block'

		# runs command as admin
		shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command)

	print(len(exes), 'files blocked!')
	runfileyn = input('Press Enter to quit or any key to continue: ')
