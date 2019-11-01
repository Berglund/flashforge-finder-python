import socket
import re

BUFFER_SIZE = 128
TIMEOUT_SECONDS = 2
PERCENTAGE_DIGITS = 3

REQUEST_TEMP_MESSAGE = '~M105\r\n'
REQUEST_PROGRESS_MESSAGE = '~M27\r\n'

PROGRESS_REGEX = re.compile('(\d*)\/(\d*)')
TEMP_REGEX = re.compile('T0:(\d*) \/(\d*)')

class Printer:
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def get_progress(self):
        """Returns current print progress as percentage"""

        data = self.make_request(REQUEST_PROGRESS_MESSAGE)
        regex_res = PROGRESS_REGEX.search(data)
        current = int(regex_res.group(1))
        max_val = int(regex_res.group(2))
        percentage = current / max_val * 100
        return round(percentage, PERCENTAGE_DIGITS)

    def get_temp(self):
        """Returns current and target temperature"""

        data = self.make_request(REQUEST_TEMP_MESSAGE)
        regex_res = TEMP_REGEX.search(data)
        current = int(regex_res.group(1))
        target = int(regex_res.group(2))
        res = {"current": current, "target": target}
        return res

    def make_request(self, data):
        soc = socket.socket()
        soc.settimeout(TIMEOUT_SECONDS)
        soc.connect((self.address, self.port))
        soc.send(data.encode())
        data = soc.recv(BUFFER_SIZE)
        soc.close()

        return data.decode()