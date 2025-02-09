from main import *

def ins_adc_imm(self) -> None:
    """
    ADC - Add with Carry, Immediate.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self["reg_a"] = t1 + t2
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_zp(self) -> None:
    """
    ADC - Add with Carry, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 + t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_zpx(self) -> None:
    """
    ADC - Add with Carry, Zero Page, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, (t2 + t3) & 0xFF)
    self["reg_a"] = t1 + t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_abs(self) -> None:
    """
    ADC - Add with Carry, Absolute.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 + t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_abx(self) -> None:
    """
    ADC - Add with Carry, Absolute, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 + t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_aby(self) -> None:
    """
    ADC - Add with Carry, Absolute, Y.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_y(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 + t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_inx(self) -> None:
    """
    ADC - Add with Carry, Indexed Indirect.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 + t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_adc_iny(self) -> None:
    """
    ADC - Add with Carry, Indirect Indexed.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, t4 = P_read_register_y(self)
    self["reg_a"] = t1 + t3 + t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_imm(self) -> None:
    """
    AND - Logical AND, Immediate.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self["reg_a"] = t1 & t2
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_zp(self) -> None:
    """
    AND - Logical AND, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 & t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_zpx(self) -> None:
    """
    AND - Logical AND, Zero Page, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, (t2 + t3) & 0xFF)
    self["reg_a"] = t1 & t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_abs(self) -> None:
    """
    AND - Logical AND, Absolute.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 & t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_abx(self) -> None:
    """
    AND - Logical AND, Absolute, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 & t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_aby(self) -> None:
    """
    AND - Logical AND, Absolute, Y.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_y(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 & t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_inx(self) -> None:
    """
    AND - Logical AND, Indexed Indirect.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 & t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_and_iny(self) -> None:
    """
    AND - Logical AND, Indirect Indexed.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, t4 = P_read_register_y(self)
    self["reg_a"] = t1 & t3 + t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_asl_acc(self) -> None:
    """
    ASL - Arithmetic Shift Left, Accumulator.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self["reg_a"] = t1 << 1
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def ins_asl_zp(self) -> None:
    """
    ASL - Arithmetic Shift Left, Zero Page.
    :return: None
    """
    address = P_fetch_byte(self)
    self, t1 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t1 << 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1

def ins_asl_zpx(self) -> None:
    """
    ASL - Arithmetic Shift Left, Zero Page, X.
    :return: None
    """
    self, t1 = P_fetch_byte(self)
    self, t2 = P_read_register_x(self)
    address = (t1 + t2) & 0xFF
    self, t3 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t3 << 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1

def ins_asl_abs(self) -> None:
    """
    ASL - Arithmetic Shift Left, Absolute.
    :return: None
    """
    address = P_fetch_word(self)
    self, t1 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t1 << 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1

def ins_asl_abx(self) -> None:
    """
    ASL - Arithmetic Shift Left, Absolute, X.
    :return: None
    """
    self, t1 = P_fetch_word(self)
    self, t2 = P_read_register_x(self)
    address = t1 + t2
    self, t3 = P_read_byte(self, address)
    self, _ = P_write_byte(self, address, t3 << 1)
    self, _ = P_evaluate_flag_n(self, M___getitem__(self["memory"], address))
    self, _ = P_evaluate_flag_z(self, M___getitem__(self["memory"], address))
    self["cycles"] += 1

def ins_bcc_rel(self) -> None:
    """
    BCC - Branch if Carry Clear.
    :return: None
    """
    if not self["flag_c"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_bcs_rel(self) -> None:
    """
    BCS - Branch if Carry Set.
    :return: None
    """
    if self["flag_c"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_beq_rel(self) -> None:
    """
    BEQ - Branch if Equal.
    :return: None
    """
    if self["flag_z"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_bit_zp(self) -> None:
    """
    BIT - Bit Test, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 & t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, t4 = P_fetch_byte(self)
    self, t5 = P_read_byte(self, t4)
    self["flag_v"] = (t5 & 0x40) != 0
    self["cycles"] += 1

def ins_bit_abs(self) -> None:
    """
    BIT - Bit Test, Absolute.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 & t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self, t4 = P_fetch_word(self)
    self, t5 = P_read_byte(self, t4)
    self["flag_v"] = (t5 & 0x40) != 0
    self["cycles"] += 1

def ins_bmi_rel(self) -> None:
    """
    BMI - Branch if Minus.
    :return: None
    """
    if self["flag_n"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_bne_rel(self) -> None:
    """
    BNE - Branch if Not Equal.
    :return: None
    """
    if not self["flag_z"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_bpl_rel(self) -> None:
    """
    BPL - Branch if Positive.
    :return: None
    """
    if not self["flag_n"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_brk_imp(self) -> None:
    """
    BRK - Force Interrupt.
    :return: None
    """
    self["flag_b"] = True
    self, _ = P_push(self, (self["program_counter"] >> 8) & 0xFF)
    self, _ = P_push(self, self["program_counter"] & 0xFF)
    self, _ = P_push(self, self["flag_c"])
    self["flag_i"] = True
    self, t1 = P_read_word(self, 0xFFFE)
    self["program_counter"] = t1
    self["cycles"] += 1

def ins_bvc_rel(self) -> None:
    """
    BVC - Branch if Overflow Clear.
    :return: None
    """
    if not self["flag_v"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1

def ins_bvs_rel(self) -> None:
    """
    BVS - Branch if Overflow Set.
    :return: None
    """
    if self["flag_v"]:
        self, t1 = P_fetch_byte(self)
        self["program_counter"] += t1
        self["cycles"] += 1








#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################







def ins_cmp_imm(self) -> None:
    """
    CMP - Compare, Immediate.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, _ = P_evaluate_flag_n(self, t1 - t2)

    self, t3 = P_read_register_a(self)
    self, t4 = P_fetch_byte(self)
    self, _ = P_evaluate_flag_z(self, t3 - t4)
    self["cycles"] += 1

def ins_cmp_zp(self) -> None:
    """
    CMP - Compare, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_n(self, t1 - t3)

    self, t4 = P_read_register_a(self)
    self, t5 = P_fetch_byte(self)
    self, t6 = P_read_byte(self, t5)
    self, _ = P_evaluate_flag_z(self, t4 - t6)
    self["cycles"] += 1

def ins_cmp_zpx(self) -> None:
    """
    CMP - Compare, Zero Page, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, (t2 + t3) & 0xFF)
    self, _ = P_evaluate_flag_n(self, t1 - t4)

    self, t5 = P_read_register_a(self)
    self, t6 = P_fetch_byte(self)
    self, t7 = P_read_register_x(self)
    self, t8 = P_read_byte(self, (t6 + t7) & 0xFF)
    self, _ = P_evaluate_flag_z(self, t5 - t8)
    self["cycles"] += 1

def ins_cmp_abs(self) -> None:
    """
    CMP - Compare, Absolute.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_n(self, t1 - t3)
    
    self, t4 = P_read_register_a(self)
    self, t5 = P_fetch_word(self)
    self, t6 = P_read_byte(self, t5)
    self, _ = P_evaluate_flag_z(self, t4 - t6)
    self["cycles"] += 1

def ins_cmp_abx(self) -> None:
    """
    CMP - Compare, Absolute, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self, _ = P_evaluate_flag_n(self, t1 - t4)

    self, t5 = P_read_register_a(self)
    self, t6 = P_fetch_word(self)
    self, t7 = P_read_register_x(self)
    self, t8 = P_read_byte(self, t6 + t7)
    self, _ = P_evaluate_flag_z(self, t5 - t8)
    self["cycles"] += 1

def ins_cmp_aby(self) -> None:
    """
    CMP - Compare, Absolute, Y.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_y(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self, _ = P_evaluate_flag_n(self, t1 - t4)
    
    self, t5 = P_read_register_a(self)
    self, t6 = P_fetch_word(self)
    self, t7 = P_read_register_y(self)
    self, t8 = P_read_byte(self, t6 + t7)
    self, _ = P_evaluate_flag_z(self, t5 - t8)
    self["cycles"] += 1

def ins_cmp_inx(self) -> None:
    """
    CMP - Compare, Indexed Indirect.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self, _ = P_evaluate_flag_n(self, t1 - t4)

    self, t5 = P_read_register_a(self)
    self, t6 = P_fetch_byte(self)
    self, t7 = P_read_register_x(self)
    self, t8 = P_read_byte(self, t6 + t7)
    self, _ = P_evaluate_flag_z(self, t5 - t8)
    self["cycles"] += 1

def ins_cmp_iny(self) -> None:
    """
    CMP - Compare, Indirect Indexed.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, t4 = P_read_register_y(self)
    self, _ = P_evaluate_flag_n(self, t1 - t3 + t4)
    
    self, t5 = P_read_register_a(self)
    self, t6 = P_fetch_byte(self)
    self, t7 = P_read_byte(self, t6)
    self, t8 = P_read_register_y(self)
    self, _ = P_evaluate_flag_z(self, t5 - t7 + t8)
    self["cycles"] += 1

def ins_cpx_imm(self) -> None:
    """
    CPX - Compare X Register, Immediate.
    :return: None
    """
    self, t1 = P_read_register_x(self)
    self, t2 = P_fetch_byte(self)
    self, _ = P_evaluate_flag_n(self, t1 - t2)
    
    self, t3 = P_read_register_x(self)
    self, t4 = P_fetch_byte(self)
    self, _ = P_evaluate_flag_z(self, t3 - t4)
    self["cycles"] += 1

def ins_cpx_zp(self) -> None:
    """
    CPX - Compare X Register, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_x(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_n(self, t1 - t3)
    
    self, t4 = P_read_register_x(self)
    self, t5 = P_fetch_byte(self)
    self, t6 = P_read_byte(self, t5)
    self, _ = P_evaluate_flag_z(self, t4 - t6)
    self["cycles"] += 1

def ins_cpx_abs(self) -> None:
    """
    CPX - Compare X Register, Absolute.
    :return: None
    """
    self, t1 = P_read_register_x(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_n(self, t1 - t3)
    
    self, t4 = P_read_register_x(self)
    self, t5 = P_fetch_word(self)
    self, t6 = P_read_byte(self, t5)
    self, _ = P_evaluate_flag_z(self, t4 - t6)
    self["cycles"] += 1

def ins_cpy_imm(self) -> None:
    """
    CPY - Compare Y Register, Immediate.
    :return: None
    """
    self, t1 = P_read_register_y(self)
    self, t2 = P_fetch_byte(self)
    self, _ = P_evaluate_flag_n(self, t1 - t2)
    
    self, t3 = P_read_register_y(self)
    self, t4 = P_fetch_byte(self)
    self, _ = P_evaluate_flag_z(self, t3 - t4)
    self["cycles"] += 1

def ins_cpy_zp(self) -> None:
    """
    CPY - Compare Y Register, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_y(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_n(self, t1 - t3)
    
    self, t4 = P_read_register_y(self)
    self, t5 = P_fetch_byte(self)
    self, t6 = P_read_byte(self, t5)
    self, _ = P_evaluate_flag_z(self, t4 - t6)
    self["cycles"] += 1

def ins_cpy_abs(self) -> None:
    """
    CPY - Compare Y Register, Absolute.
    :return: None
    """
    self, t1 = P_read_register_y(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self, _ = P_evaluate_flag_n(self, t1 - t3)
    
    self, t4 = P_read_register_y(self)
    self, t5 = P_fetch_word(self)
    self, t6 = P_read_byte(self, t5)
    self, _ = P_evaluate_flag_z(self, t4 - t6)
    self["cycles"] += 1

