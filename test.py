import flashforge

printer = flashforge.Printer("192.168.1.29", 8899)
data = printer.get_progress()
print(data)