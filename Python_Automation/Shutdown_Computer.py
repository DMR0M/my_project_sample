import os


def shutdown():
    """WARNING: Running this function shutdowns the computer"""
    sys_command = 'shutdown /s /t 0'
    os.system(sys_command)


if __name__ == '__main__':
    shutdown()
    