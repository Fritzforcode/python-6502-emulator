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

def P_push(self: dict, data: int) -> None:
    """
    Push data to stack.

    :return: None
    """
    self["memory"][self["stack_pointer"]] = data
    self["stack_pointer"] -= 1
    self["cycles"] += 1
    return self, None

def P_pop(self: dict) -> int:
    """
    Pop data from stack.

    :return: int
    """
    self["stack_pointer"] += 1
    self["cycles"] += 1
    return self, self["memory"][self["stack_pointer"] - 1]

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

def P_execute(self: dict, cycles: int = 0) -> None:
    """
    Execute code for X amount of cycles. Or until a breakpoint is reached.

    :param cycles: The number of cycles to execute
    :return: None
    """
    while (self["cycles"] < cycles) or (cycles == 0):
        self, opcode = P_fetch_byte(self)
        instr_func = eval("P_ins_" + OPCODES[opcode] + "_" + ADDRESSING[opcode])
        self, _ = instr_func(self)
    return self, None


########################################
# TODO: ENSURE CYCLE COUNT             #
########################################


"""MOT-6502 Instruction Helper Functions."""
def P_help_adc(self, operand: int) -> None:
    if self["flag_d"]:  # Decimal Mode
        low = (self["reg_a"] & 0x0F) + (operand & 0x0F) + int(self["flag_c"])
        if low > 9:
            low += 6
        high = (self["reg_a"] >> 4) + (operand >> 4) + (low > 15)
        if high > 9:
            high += 6
        result = (high << 4) | (low & 0x0F)
    else:  # Binary Mode
        result = self["reg_a"] + operand + int(self["flag_c"])

    self, _ = P_evaluate_flag_c(self, result, bcd=self["flag_d"])
    self, _ = P_evaluate_flag_z(self, result)
    self, _ = P_evaluate_flag_n(self, result)
    self["flag_v"] = bool(~(self["reg_a"] ^ operand) & (self["reg_a"] ^ result) & 0x80)
    self["reg_a"] = result & 0xFF
    return self, None

"""MOT-6502 Instructions."""
def P_ins_adc_inx(self: dict) -> None:
    """
    ADC - Add with carry, Indexed Indirect.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    zp_addr  = (t1 + self["reg_x"]) & 0xFF
    addr     = M_read_word(self["memory"], zp_addr)
    operand  = M___getitem__(self["memory"], addr)
    self, _  = P_help_adc(self, operand)
    return self, None

def P_ins_adc_iny(self: dict) -> None:
    """
    ADC - Add with carry, Indexed Indirect.

    :return: None
    """
    self, zp_addr = P_fetch_byte(self)
    base_addr = M_read_word(self["memory"], zp_addr)
    operand = M___getitem__(self["memory"], base_addr + self["reg_y"])
    self, _ = P_help_adc(self, operand)
    return self, None

def P_ins_adc_zp(self: dict) -> None:
    """
    ADC - Add with carry, Zero Page.

    :return: None
    """
    self, addr = P_fetch_byte(self)
    operand = M___getitem__(self["memory"], addr)
    self, _ = P_help_adc(self, operand)
    self["cycles"] += 2
    return self, None

def P_ins_adc_zpx(self: dict) -> None:
    """
    ADC - Add with carry, Zero Page, X-Indexed Indirect.

    :return: None
    """
    self, base_addr = P_fetch_byte(self)
    addr = (base_addr + self["reg_x"]) & 0xFF
    operand = M___getitem__(self["memory"], addr)
    self, _ = P_help_adc(self, operand)
    self["cycles"] += 3
    return self, None

def P_ins_adc_imm(self: dict) -> None:
    """
    ADC - Add with carry, Immediate.

    :return: None
    """
    self, operand = P_fetch_byte(self)
    self, _ = P_help_adc(self, operand)
    self["cycles"] += 1
    return self, None

def P_ins_adc_abx(self: dict) -> None:
    """
    ADC - Add with carry, Absolute, X.

    :return: None
    """
    self, base_addr = P_fetch_word(self)
    addr = base_addr + self["reg_x"]
    operand = M___getitem__(self["memory"], addr)
    self, _ = P_help_adc(self, operand)
    self["cycles"] += 2
    if addr > 0xFF: self["cycles"] += 1
    return self, None

def P_ins_adc_aby(self: dict) -> None:
    """
    ADC - Add with carry, Absolute, Y.

    :return: None
    """
    self, base_addr = P_fetch_word(self)
    addr = base_addr + self["reg_y"]
    operand = M___getitem__(self["memory"], addr)
    self, _ = P_help_adc(self, operand)
    self["cycles"] += 2
    if addr > 0xFF: self["cycles"] += 1
    return self, None
    
def P_ins_adc_abs(self: dict) -> None:
    """
    ADC - Add with carry, Absolute.

    :return: None
    """
    self, addr = P_fetch_word(self)
    operand = M___getitem__(self["memory"], addr)
    self, _ = P_help_adc(self, operand)
    self["cycles"] += 2
    return self, None


def P_ins_and_(self: dict) -> None:
    """
    ADC - And Memory with Accumulator, .

    :return: None
    """
    self, addr = P_fetch_word(self)
    operand = M___getitem__(self["memory"], addr)
    self, _ = P_help_adc(self, operand)
    return self, None



def P_ins_nop_imp(self: dict) -> None:
    """
    NOP - No Operation.

    :return: None
    """
    self["cycles"] += 1
    return self, None

def P_ins_clc_imp(self: dict) -> None:
    """
    CLC - Clear Carry Flag.

    :return: None
    """
    self["flag_c"] = False
    self["cycles"] += 1
    return self, None

def P_ins_cld_imp(self: dict) -> None:
    """
    CLD - Clear Decimal Mode.

    :return: None
    """
    self["flag_d"] = False
    self["cycles"] += 1
    return self, None

def P_ins_cli_imp(self: dict) -> None:
    """
    CLI - Clear Interrupt Disable.

    :return: None
    """
    self["flag_i"] = False
    self["cycles"] += 1
    return self, None

def P_ins_clv_imp(self: dict) -> None:
    """
    CLV - Clear Overflow Flag.

    :return: None
    """
    self["flag_v"] = False
    self["cycles"] += 1
    return self, None

#cmp, cpx, cpy

def P_ins_dec_zp(self: dict) -> None:
    """
    DEC - Decrement Memory, Zero Page.

    :return: None
    """
    self, address = P_fetch_byte(self)
    self, t1 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t1 - 1)

    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_dec_zpx(self: dict) -> None:
    """
    DEC - Decrement Memory, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    address = (t1 + t2) & 0xFF
    self, t3 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t3 - 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_dec_abs(self: dict) -> None:
    """
    DEC - Decrement Memory, Absolute.

    :return: None
    """
    self, address = P_fetch_word(self)
    self, t1 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t1 - 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_dec_abx(self: dict) -> None:
    """
    DEC - Decrement Memory, Absolute, X.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, t2 = P_read_register_x(self)
    address = t1 + t2
    self, t3 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t3 - 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_dex_imp(self: dict) -> None:
    """
    DEX - Decrement X Register.

    :return: None
    """
    self, t1 = P_read_register_x(self)
    self["reg_x"] = t1 - 1
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_dey_imp(self: dict) -> None:
    """
    DEY - Decrement Y Register.

    :return: None
    """
    self, t1 = P_read_register_y(self)
    self["reg_y"] = t1 - 1
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

#for

def P_ins_inc_zp(self: dict) -> None:
    """
    INC - Increment Memory, Zero Page.

    :return: None
    """
    self, address = P_fetch_byte(self)
    self, t1 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t1 + 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_inc_zpx(self: dict) -> None:
    """
    INC - Increment Memory, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    address = (t1 + t2) & 0xFF
    self, t3 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t3 + 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_inc_abs(self: dict) -> None:
    """
    INC - Increment Memory, Absolute.

    :return: None
    """
    self, address = P_fetch_word(self)
    self, t1 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t1 + 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_inc_abx(self: dict) -> None:
    """
    INC - Increment Memory, Absolute, X.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, t2 = P_read_register_x(self)
    address = t1 + t2
    self, t3 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t3 + 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1
    return self, None

def P_ins_inx_imp(self: dict) -> None:
    """
    INX - Increment X Register.

    :return: None
    """
    self, t1 = P_read_register_x(self)
    self["reg_x"] = t1 + 1
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_iny_imp(self: dict) -> None:
    """
    INY - Increment Y Register.

    :return: None
    """
    self, t1 = P_read_register_y(self)
    self["reg_y"] = t1 + 1
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

#jmp, jsr

def P_ins_lda_imm(self: dict) -> None:
    """
    LDA - Load Accumulator, Immediate.

    :return: None
    """
    self, self["reg_a"] = P_fetch_byte(self)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_lda_zp(self: dict) -> None:
    """
    LDA - Load Accumulator, Zero Page.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, self["reg_a"] = P_read_byte(self, t1)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_lda_zpx(self: dict) -> None:
    """
    LDA - Load Accumulator, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    self, self["reg_a"] = P_read_byte(self, (t1 + t2) & 0xFF)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_lda_abs(self: dict) -> None:
    """
    LDA - Load Accumulator, Absolute.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_a"] = P_read_byte(self, t1)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_lda_abx(self: dict) -> None:
    """
    LDA - Load Accumulator, Absolute, X.

    TODO: Using register X directly otherwise we use too many cycles.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_a"] = P_read_byte(self, t1 + self["reg_x"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_lda_aby(self: dict) -> None:
    """
    LDA - Load Accumulator, Absolute, Y.

    TODO: Using register Y directly otherwise we use too many cycles.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_a"] = P_read_byte(self, t1 + self["reg_y"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_lda_inx(self: dict) -> None:
    """
    LDA - Load Accumulator, Indexed Indirect.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_word(self, (t1 + self["reg_x"]) & 0xFF)
    self, self["reg_a"] = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self["cycles"] += 1
    return self, None

def P_ins_lda_iny(self: dict) -> None:
    """
    LDA - Load Accumulator, Indirect Indexed.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_word(self, t1)
    self, self["reg_a"] = P_read_byte(self, t2 + self["reg_y"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_ldx_imm(self: dict) -> None:
    """
    LDX - Load X Register, Immediate.

    :return: None
    """
    self, self["reg_x"] = P_fetch_byte(self)
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_ldx_zp(self: dict) -> None:
    """
    LDX - Load X Register, Zero Page.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, self["reg_x"] = P_read_byte(self, t1)
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_ldx_zpy(self: dict) -> None:
    """
    LDX - Load X Register, Zero Page, Y.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_y(self)
    self, self["reg_x"] = P_read_byte(self, (t1 + t2) & 0xFF)
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_ldx_abs(self: dict) -> None:
    """
    LDX - Load X Register, Absolute.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_x"] = P_read_byte(self, t1)
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_ldx_aby(self: dict) -> None:
    """
    LDX - Load X Register, Absolute, Y.

    TODO: Using register Y directly otherwise we use too many cycles.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_x"] = P_read_byte(self, t1 + self["reg_y"])
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_ldy_imm(self: dict) -> None:
    """
    LDY - Load Y Register, Immediate.

    :return: None
    """
    self, self["reg_y"] = P_fetch_byte(self)
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

def P_ins_ldy_zp(self: dict) -> None:
    """
    LDY - Load Y Register, Zero Page.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, self["reg_y"] = P_read_byte(self, t1)
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

def P_ins_ldy_zpx(self: dict) -> None:
    """
    LDY - Load Y Register, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    self, self["reg_y"] = P_read_byte(self, (t1 + t2) & 0xFF)
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

def P_ins_ldy_abs(self: dict) -> None:
    """
    LDY - Load Y Register, Absolute.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_y"] = P_read_byte(self, t1)
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

def P_ins_ldy_abx(self: dict) -> None:
    """
    LDY - Load Y Register, Absolute, X.

    TODO: Using register X directly otherwise we use too many cycles.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, self["reg_y"] = P_read_byte(self, t1 + self["reg_x"])
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

#lsr

def P_ins_sec_imp(self: dict) -> None:
    """
    SEC - Set Carry Flag.

    :return: None
    """
    self["flag_c"] = True
    self["cycles"] += 1
    return self, None

def P_ins_sed_imp(self: dict) -> None:
    """
    SED - Set Decimal Mode.

    :return: None
    """
    self["flag_d"] = True
    self["cycles"] += 1
    return self, None

def P_ins_sei_imp(self: dict) -> None:
    """
    SEI - Set Interrupt Disable.

    :return: None
    """
    self["flag_i"] = True
    self["cycles"] += 1
    return self, None

def P_ins_sta_zp(self: dict) -> None:
    """
    STA - Store Accumulator, Zero Page.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, _ = P_write_byte(self, t1, self["reg_a"])
    return self, None

def P_ins_sta_zpx(self: dict) -> None:
    """
    STA - Store Accumulator, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    self, _ = P_write_byte(self, (t1 + t2) & 0xFF, self["reg_a"])
    return self, None

def P_ins_sta_abs(self: dict) -> None:
    """
    STA - Store Accumulator, Absolute.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, _ = P_write_byte(self, t1, self["reg_a"])
    return self, None

def P_ins_sta_abx(self: dict) -> None:
    """
    STA - Store Accumulator, Absolute, X.

    TODO: Using register X directly otherwise we use too many cycles.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, t2 = P_read_byte(self, t1 + self["reg_x"])
    self, _ = P_write_byte(self, t2, self["reg_a"])
    return self, None

def P_ins_sta_aby(self: dict) -> None:
    """
    STA - Store Accumulator, Absolute, Y.

    TODO: Using register Y directly otherwise we use too many cycles.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, t2 = P_read_byte(self, t1 + self["reg_y"])
    self, _ = P_write_byte(self, t2, self["reg_a"])
    return self, None

def P_ins_sta_inx(self: dict) -> None:
    """
    STA - Store Accumulator, Indexed Indirect.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_word(self, (t1 + self["reg_x"]) & 0xFF)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_write_byte(self, t3, self["reg_a"])
    return self, None

def P_ins_sta_iny(self: dict) -> None:
    """
    LDA - Store Accumulator, Indirect Indexed.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_word(self, (t1 + self["reg_y"]) & 0xFF)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_write_byte(self, t3, self["reg_a"])
    return self, None

def P_ins_stx_zp(self: dict) -> None:
    """
    STA - Store X Register, Zero Page.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, _ = P_write_byte(self, t1, self["reg_x"])
    return self, None

def P_ins_stx_zpy(self: dict) -> None:
    """
    STA - Store Y Register, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_y(self)
    self, _ = P_write_byte(self, (t1 + t2) & 0xFF, self["reg_x"])
    return self, None

def P_ins_stx_abs(self: dict) -> None:
    """
    STA - Store X Register, Absolute.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, _ = P_write_byte(self, t1, self["reg_x"])
    return self, None

def P_ins_sty_zp(self: dict) -> None:
    """
    STA - Store Y Register, Zero Page.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, _ = P_write_byte(self, t1, self["reg_y"])
    return self, None

def P_ins_sty_zpx(self: dict) -> None:
    """
    STA - Store Y Register, Zero Page, X.

    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    self, _ = P_write_byte(self, (t1 + t2) & 0xFF, self["reg_y"])
    return self, None

def P_ins_sty_abs(self: dict) -> None:
    """
    STA - Store Y Register, Absolute.

    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, _ = P_write_byte(self, t1, self["reg_y"])
    return self, None

def P_ins_tax_imp(self: dict) -> None:
    """
    TAX - Transfer Accumulator to X.

    :return: None
    """
    self, self["reg_x"] = P_read_register_a(self)
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_tay_imp(self: dict) -> None:
    """
    TAY - Transfer Accumulator to Y.

    :return: None
    """
    self, self["reg_y"] = P_read_register_a(self)
    self, _ = P_evaluate_flag_z(self, self["reg_y"])
    self, _ = P_evaluate_flag_n(self, self["reg_y"])
    return self, None

def P_ins_tsx_imp(self: dict) -> None:
    """
    TSX - Transfer Stack Pointer to X.

    :return: None
    """
    self, self["reg_x"] = P_pop(self)
    self, _ = P_evaluate_flag_z(self, self["reg_x"])
    self, _ = P_evaluate_flag_n(self, self["reg_x"])
    return self, None

def P_ins_txa_imp(self: dict) -> None:
    """
    TXA - Transfer Register X to Accumulator.

    :return: None
    """
    self, self["reg_a"] = P_read_register_x(self)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_txs_imp(self: dict) -> None:
    """
    TXS - Transfer Register X to Stack Pointer.

    :return: None
    """
    self, _ = P_push(self, self["reg_x"])
    return self, None

def P_ins_tya_imp(self: dict) -> None:
    """
    TYA - Transfer Register Y to Accumulator.

    :return: None
    """
    self, self["reg_a"] = P_read_register_y(self)
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_pha_imp(self: dict) -> None:
    """
    PHA - Push Accumulator.

    TODO: Add check to not cross page

    :return: None
    """
    self, t1 = P_read_register_a(self)
    self["memory"] = M___setitem__(self["memory"], self["stack_pointer"], t1)
    self["stack_pointer"] -= 1
    self["cycles"] += 1
    return self, None

def P_ins_pla_imp(self: dict) -> None:
    """
    PLA - Pull Accumulator.

    TODO: Add check to not cross page

    :return: None
    """
    self["reg_a"] = M___getitem__(self["memory"], self["stack_pointer"])
    self["stack_pointer"] += 1
    self["cycles"] += 1
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    return self, None

def P_ins_php_imp(self: dict) -> None:
    """
    Push Processor Statys, Implied.

    return: None
    """
    flags = 0x00
    if self["flag_n"]:
        flags = flags | (1 << 1)
    if self["flag_v"]:
        flags = flags | (1 << 2)
    if self["flag_b"]:
        flags = flags | (1 << 3)
    if self["flag_d"]:
        flags = flags | (1 << 4)
    if self["flag_i"]:
        flags = flags | (1 << 5)
    if self["flag_z"]:
        flags = flags | (1 << 6)
    if self["flag_c"]:
        flags = flags | (1 << 7)
    self, _ = P_push(self, flags)
    self["cycles"] += 1
    return self, None

def P_ins_plp_imp(self: dict) -> None:
    """
    Pull Processor Status.

    TODO: Implement instruction and test
    TODO: Add check to not cross page

    :return: None
    """
    self, flags = P_pop(self)
    # print(flags)
    if not flags & (1 << 1):
        self["flag_n"] = False
    if not flags & (1 << 2):
        self["flag_v"] = False
    if not flags & (1 << 3):
        self["flag_b"] = False
    if not flags & (1 << 4):
        self["flag_d"] = False
    if not flags & (1 << 5):
        self["flag_i"] = False
    if not flags & (1 << 6):
        self["flag_z"] = False
    if not flags & (1 << 7):
        self["flag_c"] = False
    self["cycles"] += 2
    return self, None












"""Emulation of the MOT-6502 memory."""

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
