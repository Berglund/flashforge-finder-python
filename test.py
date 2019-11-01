import flashforge

printer = flashforge.Printer("192.168.1.29", 8899)
data = printer.get_progress()
print(data)

data = printer.get_temp()
print("Current: %d, target: %d" % (data["current"], data["target"]))