from subprocess import call
from datetime import datetime
from snd import Backup

def main():
    # Get current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    # 开始进行备份
    Backup()