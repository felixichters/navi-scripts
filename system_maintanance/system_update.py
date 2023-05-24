import subprocess

print()
print("check for failed systemd services...")
print()
check_errors = subprocess.run(["systemctl", "--failed"], capture_output=True, text=True)   
print(check_errors.stdout)
print()

print("update packages via pacman...")
print()
pacman = subprocess.Popen(['pacman', '-Syu'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
user_input = input()
pacman.stdin.write(user_input + '\n')
pacman.stdin.flush()
output, error = pacman.communicate()
print()

print("update packages via yay...")
print()
yay = subprocess.Popen(['yay', '-Syu'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
user_input = input()
yay.stdin.write(user_input + '\n')
yay.stdin.flush()
output, error = yay.communicate()
print()
