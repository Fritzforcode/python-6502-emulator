"""Emulation of the MOT-6502 Processor."""

ADDRESSING = [
    #  0  |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |  A   |  B   |  C   |  D   |  E   |  F   |
    "imp", "inx", "imp", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "acc", "imm", "abs", "abs", "abs", "abs",  # 0
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpx", "zpx", "imp", "aby", "imp", "aby", "abx", "abx", "abx", "abx",  # 1
    "abs", "inx", "imp", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "acc", "imm", "abs", "abs", "abs", "abs",  # 2
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpx", "zpx", "imp", "aby", "imp", "aby", "abx", "abx", "abx", "abx",  # 3
    "imp", "inx", "imp", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "acc", "imm", "abs", "abs", "abs", "abs",  # 4
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpx", "zpx", "imp", "aby", "imp", "aby", "abx", "abx", "abx", "abx",  # 5
    "imp", "inx", "imp", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "acc", "imm", "ind", "abs", "abs", "abs",  # 6
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpx", "zpx", "imp", "aby", "imp", "aby", "abx", "abx", "abx", "abx",  # 7
    "imm", "inx", "imm", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "imp", "imm", "abs", "abs", "abs", "abs",  # 8
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpy", "zpy", "imp", "aby", "imp", "aby", "abx", "abx", "aby", "aby",  # 9
    "imm", "inx", "imm", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "imp", "imm", "abs", "abs", "abs", "abs",  # A
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpy", "zpy", "imp", "aby", "imp", "aby", "abx", "abx", "aby", "aby",  # B
    "imm", "inx", "imm", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "imp", "imm", "abs", "abs", "abs", "abs",  # C
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpx", "zpx", "imp", "aby", "imp", "aby", "abx", "abx", "abx", "abx",  # D
    "imm", "inx", "imm", "inx", "zp",  "zp",  "zp",  "zp",  "imp", "imm", "imp", "imm", "abs", "abs", "abs", "abs",  # E
    "rel", "iny", "imp", "iny", "zpx", "zpx", "zpx", "zpx", "imp", "aby", "imp", "aby", "abx", "abx", "abx", "abx",  # F
]

["imp", "inx", "zp", "imm", "acc", "abs", "rel", "iny", "zpx", "aby", "abx", "ind", "zpy"]

"imp"
"acc"
"rel"
"ind"
"zpy"

"imm"
"zp"
"zpx"
"abs"
"abx"
"aby"
"inx"
"iny"

OPCODES = [
    #  0  |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |  A   |  B   |  C   |  D   |  E   |  F   |
    "brk", "ora", "nop", "slo", "nop", "ora", "asl", "slo", "php", "ora", "asl", "nop", "nop", "ora", "asl", "slo",  # 0
    "bpl", "ora", "nop", "slo", "nop", "ora", "asl", "slo", "clc", "ora", "nop", "slo", "nop", "ora", "asl", "slo",  # 1
    "jsr", "and", "nop", "rla", "bit", "and", "rol", "rla", "plp", "and", "rol", "nop", "bit", "and", "rol", "rla",  # 2
    "bmi", "and", "nop", "rla", "nop", "and", "rol", "rla", "sec", "and", "nop", "rla", "nop", "and", "rol", "rla",  # 3
    "rti", "eor", "nop", "sre", "nop", "eor", "lsr", "sre", "pha", "eor", "lsr", "nop", "jmp", "eor", "lsr", "sre",  # 4
    "bvc", "eor", "nop", "sre", "nop", "eor", "lsr", "sre", "cli", "eor", "nop", "sre", "nop", "eor", "lsr", "sre",  # 5
    "rts", "adc", "nop", "rra", "nop", "adc", "ror", "rra", "pla", "adc", "ror", "nop", "jmp", "adc", "ror", "rra",  # 6
    "bvs", "adc", "nop", "rra", "nop", "adc", "ror", "rra", "sei", "adc", "nop", "rra", "nop", "adc", "ror", "rra",  # 7
    "nop", "sta", "nop", "sax", "sty", "sta", "stx", "sax", "dey", "nop", "txa", "nop", "sty", "sta", "stx", "sax",  # 8
    "bcc", "sta", "nop", "nop", "sty", "sta", "stx", "sax", "tya", "sta", "txs", "nop", "nop", "sta", "nop", "nop",  # 9
    "ldy", "lda", "ldx", "lax", "ldy", "lda", "ldx", "lax", "tay", "lda", "tax", "nop", "ldy", "lda", "ldx", "lax",  # A
    "bcs", "lda", "nop", "lax", "ldy", "lda", "ldx", "lax", "clv", "lda", "tsx", "lax", "ldy", "lda", "ldx", "lax",  # B
    "cpy", "cmp", "nop", "dcp", "cpy", "cmp", "dec", "dcp", "iny", "cmp", "dex", "nop", "cpy", "cmp", "dec", "dcp",  # C
    "bne", "cmp", "nop", "dcp", "nop", "cmp", "dec", "dcp", "cld", "cmp", "nop", "dcp", "nop", "cmp", "dec", "dcp",  # D
    "cpx", "sbc", "nop", "isb", "cpx", "sbc", "inc", "isb", "inx", "sbc", "nop", "sbc", "cpx", "sbc", "inc", "isb",  # E
    "beq", "sbc", "nop", "isb", "nop", "sbc", "inc", "isb", "sed", "sbc", "nop", "isb", "nop", "sbc", "inc", "isb",  # F
]

BYTEORDER = "big"

"""MOT-6502 Processor."""

def P___init__(memory: dict) -> dict:
    """
    Initialize the processor.

    :param memory: The memory to use
    :return: None
    """
    self = {}
    self["memory"] = memory
    self["reg_a"] = 0  # Accumlator A
    self["reg_y"] = 0  # Incex Register Y
    self["reg_x"] = 0  # Incex Register X

    self["program_counter"] = 0  # Program Counter PC
    self["stack_pointer"]   = 0  # Stack Pointer S
    self["cycles"]          = 0  # Cycles used

    self["flag_c"] = True  # Status flag - Carry Flag
    self["flag_z"] = True  # Status flag - Zero Flag
    self["flag_i"] = True  # Status flag - Interrupt Disable
    self["flag_d"] = True  # Status flag - Decimal Mode Flag
    self["flag_b"] = True  # Status flag - Break Command
    self["flag_v"] = True  # Status flag - Overflow Flag
    self["flag_n"] = True  # Status flag - Negative Flag
    return self

def P_reset(self: dict) -> None:
    """
    Reset processor to initial state.

    :return: None
    """
    self["program_counter"] = 0xFCE2  # Hardcoded start vector post-reset
    self["stack_pointer"]   = 0x01FD  # Hardcoded stack pointer post-reset
    self["cycles"]          = 0

    self["flag_i"] = True
    self["flag_d"] = False
    self["flag_b"] = True
    return self, None

def P_fetch_byte(self: dict) -> int:
    """
    Fetch a byte from memory.

    :param address: The address to read from
    :return: int
    """
    self, data = P_read_byte(self, self["program_counter"])
    self["program_counter"] += 1
    return self, data

def P_fetch_word(self: dict) -> int:
    """
    Fetch a word from memory.

    :param address: The address to read from
    :return: int
    """
    self, data = P_read_word(self, self["program_counter"])
    self["program_counter"] += 2
    return self, data

def P_read_byte(self: dict, address: int) -> int:
    """
    Read a byte from memory.

    :param address: The address to read from
    :return: int
    """
    data = M___getitem__(self["memory"], address)
    self["cycles"] += 1
    return self, data

def P_read_word(self: dict, address: int) -> int:
    """
    Read a word from memory.

    :param address: The address to read from
    :return: int
    """
    if BYTEORDER == "little":
        self, t1 = P_read_byte(self, address    )
        self, t2 = P_read_byte(self, address + 1)
        data = t1 | (t2  << 8)
    else:
        self, t1 = P_read_byte(self, address    )
        self, t2 = P_read_byte(self, address + 1)
        data = (t1 << 8) | t2
    return self, data

def P_write_byte(self: dict, address: int, value: int) -> None:
    """
    Write a byte to memory.

    :param address: The address to write to
    :param value: The value to write
    :return: None
    """
    memory = M___setitem__(self["memory"], address, value & 0xFF)
    self["cycles"] += 1
    return self, None

def P_write_word(self: dict, address: int, value: int) -> None:
    """
    Split a word to two bytes and write to memory.

    :param address: The address to write to
    :param value: The value to write
    :return: None
    """
    if BYTEORDER == "little":
        self, _ = P_write_byte(self, address,      value       & 0xFF)
        self, _ = P_write_byte(self, address + 1, (value >> 8) & 0xFF)
    else:
        self, _ = P_write_byte(self, address,     (value >> 8) & 0xFF)
        self, _ = P_write_byte(self, address + 1,  value       & 0xFF)
    return self, None

def P_read_register_a(self: dict) -> int:
    """
    Read the A register.

    :return: int
    """
    self["cycles"] += 1
    return self, self["reg_a"]

def P_read_register_x(self: dict) -> int:
    """
    Read the X register.

    :return: int
    """
    self["cycles"] += 1
    return self, self["reg_x"]

def P_read_register_y(self: dict) -> int:
    """
    Read the Y register.

    :return: int
    """
    self["cycles"] += 1
    return self, self["reg_y"]

def P_push_byte(self: dict, data: int) -> None:
    """
    Push a byte to stack.

    :return: None
    """
    self["memory"] = M___setitem__(self["memory"], self["stack_pointer"], data)
    self["stack_pointer"] -= 1
    self["cycles"] += 1
    return self, None

def P_push_word(self: dict, data: int) -> None:
    if BYTEORDER == "little":
        self, _ = P_push_byte(self,  data       & 0xFF)
        self, _ = P_push_byte(self, (data >> 8) & 0xFF)
    else:
        self, _ = P_push_byte(self, (data >> 8) & 0xFF)
        self, _ = P_push_byte(self,  data       & 0xFF)
    return self, None

def P_pop_byte(self: dict) -> int:
    """
    Pop data from stack.

    :return: int
    """
    self["stack_pointer"] += 1
    self["cycles"] += 1
    data = M___getitem__(self["memory"], self["stack_pointer"])
    return self, data

def P_pop_word(self: dict) -> None:
    if BYTEORDER == "little":
        self, t1 = P_pop_byte(self)
        self, t2 = P_pop_byte(self)
        data = (t1 << 8) | t2
    else:
        self, t1 = P_pop_byte(self)
        self, t2 = P_pop_byte(self)
        data = t1 | (t2 << 8)
    return self, data

def P_evaluate_flag_c(self: dict, data: int, bcd: bool = False) -> None:
    """
    Evaluate carry flag.

    :param data: The data to evaluate
    :param bcd: Wether the data is in BCD format
    :return: None
    """
    if bcd:
        self["flag_c"] = (data >> 8) > 0
    else:
        self["flag_c"] = data > 0xFF
    return self, None

def P_evaluate_flag_n(self: dict, data: int) -> None:
    """
    Evaluate negative flag.

    :param data: The data to evaluate
    :return: None
    """
    self["flag_n"] = (data & 0x80) != 0
    return self, None

def P_evaluate_flag_z(self: dict, data: int) -> None:
    """
    Evaluate the Zero Flag.

    :param data: The data to evaluate
    :return: None
    """
    if data == 0:
        self["flag_z"] = True
    else:
        self["flag_z"] = False
    return self, None

def P_evaluate_flags_nz_a(self: dict) -> None:
    """
    Evaluate the Zero and Negative Flags for the Accumulator.

    :return: None
    """
    self, _ = P_evaluate_flags_nz(self, self["reg_a"])
    return self, None

def P_evaluate_flags_nz_x(self: dict) -> None:
    """
    Evaluate the Zero and Negative Flags for the X Register.

    :return: None
    """
    self, _ = P_evaluate_flags_nz(self, self["reg_x"])
    return self, None

def P_evaluate_flags_nz_y(self: dict) -> None:
    """
    Evaluate the Zero and Negative Flags for the Y Register.

    :return: None
    """
    self, _ = P_evaluate_flags_nz(self, self["reg_y"])
    return self, None

def P_evaluate_flags_nz(self: dict, data: int) -> None:
    """
    Evaluate the Zero and Negative Flags.

    :param data: The data to evaluate
    :return: None
    """
    self, _ = P_evaluate_flag_n(self, data)
    self, _ = P_evaluate_flag_z(self, data)
    return self, None

def P_execute(self: dict, cycles: int = 0) -> None:
    """
    Execute code for X amount of cycles. Or until a breakpoint is reached.

    :param cycles: The number of cycles to execute
    :return: None
    """
    while (self["cycles"] < cycles) or (cycles == 0):
        self, opcode_num = P_fetch_byte(self)
        opcode = OPCODES[opcode_num]
        addressing_mode = ADDRESSING[opcode_num]
        
        instr_func = eval("P_ins" + opcode)
        assert instr_func != None, f"Opcode '{opcode}' is not implemented."
        
        if addressing_mode in {"imm", "zp", "zpx", "abs", "abx", "aby", "inx", "iny",   "rel"}:
            addressing_func = eval("P_addressing_" + addressing_mode)
            self, operand, args = addressing_func(self, opcode)
            self, _ = instr_func(self, operand, *args)
        else:
            self, _ = instr_func(self, addressing_mode)
        
        
        

        # instr_func = eval("P_ins_" + OPCODES[opcode] + "_" + ADDRESSING[opcode])
        # self, _ = instr_func(self)
    return self, None

"""Addressing for the MOT-6502"""
def P_addressing_imm(self, opcode):
    """Immediate Addressing - Fetches operand directly from the instruction."""
    self, operand = P_fetch_byte(self)
    return self, operand, ()  # No memory address involved


def P_addressing_zp(self, opcode):
    """Zero Page Addressing - Fetches operand from zero page address."""
    self, address = P_fetch_byte(self)
    self, operand = P_read_byte(self, address)
    if opcode in {"sta", "stx", "sty"}:
        self, _ = P_adjust_cycles(-1)
    return self, operand, (address,)

def P_addressing_zpx(self, opcode):
    """Zero Page,X Addressing - Fetches operand from zero page address + X (wraps at 0xFF)."""
    self, base_address = P_fetch_byte(self)
    self, offset = P_read_register_x(self)
    address = (base_address + offset) & 0xFF  # Zero-page wrap-around
    self, operand = P_read_byte(self, address)
    if opcode in {"sta", "stx", "sty"}:
        self, _ = P_adjust_cycles(-1)
    return self, operand, (address,)

def P_addressing_abs(self, opcode):
    """Absolute Addressing - Fetches operand from a full 16-bit address."""
    self, address = P_fetch_word(self)
    self, operand = P_read_byte(self, address)
    if opcode in {"sta", "stx", "sty"}:
        self, _ = P_adjust_cycles(-1)
    return self, operand, (address,)

def P_addressing_abx(self, opcode):
    """Absolute,X Addressing - Adds X to a 16-bit base address."""
    self, base_address = P_fetch_word(self)
    self, offset = P_read_register_x(self)
    address = (base_address + offset) & 0xFFFF  # Full address wrap-around
    self, operand = P_read_byte(self, address)
    return self, operand, (address,)

def P_addressing_aby(self, opcode):
    """Absolute,Y Addressing - Adds Y to a 16-bit base address."""
    self, base_address = P_fetch_word(self)
    self, offset = P_read_register_y(self)
    address = (base_address + offset) & 0xFFFF
    self, operand = P_read_byte(self, address)
    return self, operand, (address,)

def P_addressing_inx(self, opcode):
    """
    Indexed Indirect Addressing (Indirect,X) - Fetches a 16-bit pointer from zero-page.
    
    Steps:
    1. Fetch zero-page base address.
    2. Add X to base address (wrap at 0xFF).
    3. Fetch 16-bit pointer from zero-page.
    4. Read operand from final address.
    """
    self, base_address = P_fetch_byte(self)
    self, offset = P_read_register_x(self)
    zp_address = (base_address + offset) & 0xFF  # Zero-page wrap-around
    self, final_address = P_read_word(self, zp_address)  # Fetch 16-bit address
    self, operand = P_read_byte(self, final_address)  # Read from computed address
    return self, operand, (final_address,)

def P_addressing_iny(self, opcode):
    """
    Indirect Indexed Addressing (Indirect),Y - Reads 16-bit pointer from zero-page, then adds Y.
    
    Steps:
    1. Fetch zero-page base address.
    2. Read 16-bit pointer from zero-page.
    3. Add Y to pointer to get final address.
    4. Read operand from final address.
    """
    self, base_address = P_fetch_byte(self)
    self, zp_pointer = P_read_word(self, base_address)  # Fetch 16-bit address
    self, offset = P_read_register_y(self)
    final_address = (zp_pointer + offset) & 0xFFFF  # Handle wrapping
    self, operand = P_read_byte(self, final_address)  # Read from computed address
    return self, operand, (final_address,)

def P_addressing_rel(self, opcode):
    self, operand = P_fetch_byte(self)
    return self, operand, ()

"""Subroutines for thr MOT-6502"""
def P_adjust_cycles(self, cycles: int):
    """ Adjust the cycle count for accuracy """
    self["cycles"] += cycles
    return self, None

def bcd_to_decimal(bcd):
    decimal = 0
    place = 1
    while bcd > 0:
        decimal += (bcd % 10) * place
        bcd //= 10
        place *= 10
    return decimal

def decimal_to_bcd(decimal):
    bcd = 0
    place = 1
    while decimal > 0:
        bcd += (decimal % 10) * place
        decimal //= 10
        place *= 10
    return bcd

def BTIWISE(mode, a, b):
    pass

def ADD(a, b, bcd:bool):
    if bcd:
        decimal1 = bcd_to_decimal(a)
        decimal2 = bcd_to_decimal(b)
        result_decimal = decimal1 + decimal2
        result_bcd = decimal_to_bcd(result_decimal)
        return result_bcd & 0xFF
    else:
        return (a + b)    & 0xFF

def SUB(a, b, bcd:bool):
    if bcd:
        decimal1 = bcd_to_decimal(a)
        decimal2 = bcd_to_decimal(b)
        result_decimal = decimal1 - decimal2
        result_bcd = decimal_to_bcd(result_decimal)
        return result_bcd & 0xFF
    else:
        return (a + b)    & 0xFF

############################################################################################################
#                                          MOT-6502 Instructions.                                          #
############################################################################################################

def P_ins_nop(self: dict, mode: str) -> None:
    """
    NOP - No Operation.

    :return: None
    """
    self["cycles"] += 1
    return self, None

def P_ins_adc(self: dict, operand: int, *args) -> None:
    """
    ADC - Add with Carry.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self["reg_a"] = ADD(old_value, operand, bcd=self["flag_d"])
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1
    return self, None

def P_ins_and(self: dict, operand: int, *args) -> None:
    """
    AND - Logical AND.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self["reg_a"] = old_value & operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1
    return self, None

def P_ins_asl(self: dict, operand: int, *args) -> None:
    """
    ASL - Arithmetic Shift Left.
    :return: None
    """
    self["reg_a"] = operand << 1
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1
    return self, None

def P_ins_bcc(self: dict, operand: int, *args) -> None:
    """
    BCC - Branch if Carry Clear.
    :return: None
    """
    if not self["flag_c"]:
        self["program_counter"] += operand
        self["cycles"] += 1
    return self, None

def P_ins_bcs(self: dict, operand: int, *args) -> None:
    """
    BCS - Branch if Carry Set.
    :return: None
    """
    if self["flag_c"]:
        self["program_counter"] += operand
        self["cycles"] += 1
    return self, None

def P_ins_beq(self: dict, operand: int, *args) -> None:
    """
    BEQ - Branch if Equal.
    :return: None
    """
    if self["flag_z"]:
        self["program_counter"] += operand
        self["cycles"] += 1
    return self, None

def P_ins_bit(self: dict, operand: int, *args) -> None:
    """
    BIT - Bit Test.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self["flag_n"] = bool(old_value & 0b10000000)
    self["flag_v"] = bool(old_value & 0b01000000)
    self["flag_z"] = (old_value & operand) == 0
    return self, None

def P_ins_bmi(self: dict, operand: int, *args) -> None:
    """
    BMI - Branch if Minus.
    :return: None
    """
    if self["flag_n"]:
        self["program_counter"] += operand
        self["cycles"] += 1
    return self, None

def P_ins_bne(self: dict, operand: int, *args) -> None:
    """
    BNE - Branch if Not Equal.
    :return: None
    """
    if not self["flag_z"]:
        self["program_counter"] += operand
        self["cycles"] += 1
    return self, None

def P_ins_bpl(self: dict, operand: int, *args) -> None:
    """
    BPL - Branch if Positive.
    :return: None
    """
    if not self["flag_n"]:
        self["program_counter"] += operand
        self["cycles"] += 1
    return self, None

def P_ins_brk(self: dict) -> None:
    """
    BRK - Force Interrupt.
    :return: None
    """
    # Increment PC (BRK uses an implied operand, so PC should skip the next byte)
    self["pc"] += 1

    # Push the Program Counter onto the stack (high byte first)
    pc = self["pc"]
    self, _ = P_push_stack(self, (pc >> 8) & 0xFF)  # High byte
    self, _ = P_push_stack(self, pc & 0xFF)         # Low byte

    # Push the Status Register onto the stack with Break flag set (B = 1)
    self["status"] |= 0b00010000  # Set Break flag
    self, _ = P_push_stack(self, self["status"])

    # Fetch the IRQ/BRK vector at 0xFFFE-0xFFFF
    self, low = P_read_byte(self, 0xFFFE)
    self, high = P_read_byte(self, 0xFFFF)
    self["pc"] = (high << 8) | low  # Set PC to the interrupt handler address

    # Set Interrupt Disable flag (I = 1)
    self["status"] |= 0b00000100

    # BRK takes 7 cycles
    self["cycles"] += 7

############################################################################################################
#                                     Emulation of the MOT-6502 memory.                                    #
############################################################################################################

"""Memory bank for MOT-6502 systems."""

def M___init__(size: int = None) -> dict:
    """
    Initialize the memory.

    :param size: The size of the memory
    :return: None
    """
    self = {}
    if size is None:
        size = 0xFFFF
    if size < 0x0200:
        raise ValueError("Memory size is not valid")
    if size > 0xFFFF:
        raise ValueError("Memory size is not valid")
    self["size"] = size
    self["memory"] = [0] * self["size"]
    return self

def M___getitem__(self: dict, address: int) -> int:
    """
    Get the value at the specified address.

    :param address: The address to read from
    :return: The value at the specified address
    """
    if 0x0000 < address > 0xFFFF:
        raise ValueError("Memory address is not valid")
    return self["memory"][address]

def M_read_word(self: dict, address: int) -> int:
    """
    Get the value at the specified and the following address.

    :param address: The lower address to read from
    :return: The value at the specified and following address
    """
    if BYTEORDER == "little":
        t1 = M___getitem__(self, address    )
        t2 = M___getitem__(self, address + 1) << 8
    else:
        t1 = M___getitem__(self, address    ) << 8
        t2 = M___getitem__(self, address + 1)
    return t1 | t2

def M___setitem__(self: dict, address: int, value: int) -> dict:
    """
    Set the value at the specified address.

    :param address: The address to write to
    :param value: The value to write to the address
    :return: None
    """
    if 0x0000 < address > 0xFFFF:
        raise ValueError("Memory address is not valid")
    if value > 2**8:
        raise ValueError("Value too large")
    self["memory"][address] = value
    return self
