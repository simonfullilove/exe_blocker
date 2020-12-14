from tkinter import filedialog
import os
# shell required to run os commands as admin
import win32com.shell.shell as shell
import tkinter as tk

root = tk.Tk()
root.title('Exe Blocker')

canvas1 = tk.Canvas(root, width=300, height=0)
canvas1.pack()

def block_exes(path):
    # crawls path directory and creates array of executables found in it and subdirectories
    exes = []
    for folder in os.walk(path):
        for found_file in folder[2]:
            if found_file[-4:].lower() == '.exe':
                fullpath = folder[0] + '\\' + found_file
                exes.append(fullpath)
                output.insert(tk.END, 'Executable found: ' + fullpath + '\n')
                output.see(tk.END)
    # if any exes found, creates a one line cmd command creating rule for each exe
    if len(exes) > 0:
        command = ''
        for exe in exes:
            if command != '':
                command += '&&'
            command += 'netsh advfirewall firewall add rule name="BlockProgram" dir=out program="' + exe + '" profile=any action=block'
        # runs command as admin
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + command)
    output.insert(tk.END, str(len(exes)) + ' files blocked!' + '\n')
    output.see(tk.END)

def choose_directory():
    dirpath = filedialog.askdirectory(title='Choose a folder')
    dirpath = dirpath.replace('/','\\')
    block_exes(dirpath)

button1 = tk.Button(text='Select Directory...', command=choose_directory, bg='white', fg='black')
button1.pack(padx = 5, anchor='nw')

canvas1 = tk.Canvas(root, width=300, height=0)
canvas1.pack()

output = tk.Text(root,width=120,height=30, bg='white', fg='black')
output.pack()

label1 = tk.Label(root, text="Exe Blocker v1.0")
label1.pack()

root.mainloop()