import serial
ser = serial.Serial('COM3')  # open serial port
print(ser.name)         # check which port was really used
command=b'\x55\x16\x04\xfc\x02\x09\x64\x00\x40\x07\x30\x55\x53\x00\x00\x55\x53\x00\x00\x01\x1f\xe5'    
ser.write(command)
ser.close()             # close port
