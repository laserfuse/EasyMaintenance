import subprocess

def run_cmd(cmd):
    subprocess.run(cmd, shell=True)

def run_cmd_in_cmd(command):
    subprocess.Popen(f'start cmd /k {command}', shell=True)

def run_ps_admin(cmd):
    subprocess.run([
        "powershell", 
        "-NoProfile", 
        "-Command", 
        f"Start-Process powershell -Verb Runas -ArgumentList '-NoProfile -Command{cmd}'"
        ])