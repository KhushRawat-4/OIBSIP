from datetime import datetime 
import subprocess


def launch_application(command, app_name):
    """
    Launch an application safely.
    """
    try:
        subprocess.Popen([command])
        return True
    except FileNotFoundError:
        return False
def get_current_time():
    """ return the current time."""
    return datetime.now().strftime("%I:%M %p")

def get_current_date():

    return datetime.now().strftime("%A, %d %B %Y" )
