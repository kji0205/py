# import app
import time
from time import sleep

class Dialog(object):
    # def __init__(self, save_dir):
    #   self.save_dir = save_dir
    pass

# save_dir = Dialog(app.prefs.get('save_dir'))
save_dialog = Dialog()

sleep(3)

def show():
    import app
    save_dialog.save_dir = app.prefs.get('save_dir')


def configure():
    save_dialog.save_dir = app.prefs.get('save_dir')   