from ota_update.main.ota_updater import OTAUpdater
import machine
import time


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('url-to-your-github-project')
    ota_updater.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    pin=machine.Pin(2, machine.Pin.OUT)
    while(1):
        pin.value(1)
        time.sleep(1)
        pin.value(0)
        time.sleep(1)

def boot():
    download_and_install_update_if_available()
    start()


boot()
