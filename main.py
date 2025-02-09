from m6502 import *

start = 0#0xFCE2
program = [0xA9, 11, 0x79, 0x02, 0x00]

#0b  0101 0110  56 
#0b  1000 0001  81
#0b  1101 0111 137
#0b 10011 0111

memory = M___init__(0x03FF)
for i, item in enumerate(program):
    memory = M___setitem__(memory, start+i, item)
#M___setitem__(memory, 512, 29)
M___setitem__(memory, 512+3, 56)
#M___setitem__(memory, 0x20+6, 1)
#M___setitem__(memory, 257, 97)

cpu = P___init__(memory)
cpu["flag_d"] = False
cpu["flag_c"] = False
cpu["reg_y"] = 3
print(cpu)
print(bin(cpu["reg_a"]))
cpu, _ = P_execute(cpu, 2)
print(cpu)
print(bin(cpu["reg_a"]))
cpu, _ = P_execute(cpu, 4)
print(cpu)
print(bin(cpu["reg_a"]))
