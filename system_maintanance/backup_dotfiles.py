import os 
import subprocess 

#backup dotfiles

def git_cmd(command, cwd=None): #function for git commands 
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd) 
    output, error = process.communicate()
    return output, error

home_dir = os.path.expanduser('~')  
git_dir = os.path.join(home_dir, '.config/') #directory where git commands execute 

#git add command configuration 
tracked_files = ['alacritty/ ', 'btop/ ', 'nitrogen/ ', 'nvim/ ', 'picom/ ', 'ranger/ ', 'rofi/ ','xmonad/ ', 'xmobar/ ', 'xournalpp/ ']
add_cmd = 'git add ' + ''.join(tracked_files)
output, error = git_cmd(add_cmd, cwd=git_dir)

if error: 
    print("ERROR: git add: ", error.decode('utf-8'))
else: 
    print("DONE: git add")
#
#git commit command configuration 
user_input = input("custom commit message (j/n): ")
if user_input == 'n':
    commit_message = 'dotfiles update'
else:
    commit_message = input("custom commit message: ")

commit_cmd = 'git commit -m "' + commit_message + '"'
output, error = git_cmd(commit_cmd, cwd=git_dir)

if error: 
    print("ERROR: git commit: ", error.decode('utf-8'))
else: 
    print("DONE: git commit")

#status of current git repo 
print("ready to push") 