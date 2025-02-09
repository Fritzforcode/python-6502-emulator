def ins_adc_imm(self) -> None:
    """
    ADC - Add with Carry, Immediate.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.fetch_byte()
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_zp(self) -> None:
    """
    ADC - Add with Carry, Zero Page.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_byte())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_zpx(self) -> None:
    """
    ADC - Add with Carry, Zero Page, X.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte((self.fetch_byte() + self.read_register_x()) & 0xFF)
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_abs(self) -> None:
    """
    ADC - Add with Carry, Absolute.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_word())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_abx(self) -> None:
    """
    ADC - Add with Carry, Absolute, X.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_word() + self.read_register_x())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_aby(self) -> None:
    """
    ADC - Add with Carry, Absolute, Y.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_word() + self.read_register_y())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_inx(self) -> None:
    """
    ADC - Add with Carry, Indexed Indirect.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_byte() + self.read_register_x())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_adc_iny(self) -> None:
    """
    ADC - Add with Carry, Indirect Indexed.
    :return: None
    """
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_byte()) + self.read_register_y()
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_imm(self) -> None:
    """
    AND - Logical AND, Immediate.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.fetch_byte()
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_zp(self) -> None:
    """
    AND - Logical AND, Zero Page.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_byte())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_zpx(self) -> None:
    """
    AND - Logical AND, Zero Page, X.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte((self.fetch_byte() + self.read_register_x()) & 0xFF)
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_abs(self) -> None:
    """
    AND - Logical AND, Absolute.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_word())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_abx(self) -> None:
    """
    AND - Logical AND, Absolute, X.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_word() + self.read_register_x())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_aby(self) -> None:
    """
    AND - Logical AND, Absolute, Y.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_word() + self.read_register_y())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_inx(self) -> None:
    """
    AND - Logical AND, Indexed Indirect.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_byte() + self.read_register_x())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_and_iny(self) -> None:
    """
    AND - Logical AND, Indirect Indexed.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_byte()) + self.read_register_y()
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_asl_acc(self) -> None:
    """
    ASL - Arithmetic Shift Left, Accumulator.
    :return: None
    """
    self.reg_a = self.read_register_a() << 1
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.cycles += 1

def ins_asl_zp(self) -> None:
    """
    ASL - Arithmetic Shift Left, Zero Page.
    :return: None
    """
    address = self.fetch_byte()
    self.write_byte(address, self.read_byte(address) << 1)
    self.evaluate_flag_n(self.memory[address])
    self.evaluate_flag_z(self.memory[address])
    self.cycles += 1

def ins_asl_zpx(self) -> None:
    """
    ASL - Arithmetic Shift Left, Zero Page, X.
    :return: None
    """
    address = (self.fetch_byte() + self.read_register_x()) & 0xFF
    self.write_byte(address, self.read_byte(address) << 1)
    self.evaluate_flag_n(self.memory[address])
    self.evaluate_flag_z(self.memory[address])
    self.cycles += 1

def ins_asl_abs(self) -> None:
    """
    ASL - Arithmetic Shift Left, Absolute.
    :return: None
    """
    address = self.fetch_word()
    self.write_byte(address, self.read_byte(address) << 1)
    self.evaluate_flag_n(self.memory[address])
    self.evaluate_flag_z(self.memory[address])
    self.cycles += 1

def ins_asl_abx(self) -> None:
    """
    ASL - Arithmetic Shift Left, Absolute, X.
    :return: None
    """
    address = self.fetch_word() + self.read_register_x()
    self.write_byte(address, self.read_byte(address) << 1)
    self.evaluate_flag_n(self.memory[address])
    self.evaluate_flag_z(self.memory[address])
    self.cycles += 1

def ins_bcc_rel(self) -> None:
    """
    BCC - Branch if Carry Clear.
    :return: None
    """
    if not self.flag_c:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_bcs_rel(self) -> None:
    """
    BCS - Branch if Carry Set.
    :return: None
    """
    if self.flag_c:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_beq_rel(self) -> None:
    """
    BEQ - Branch if Equal.
    :return: None
    """
    if self.flag_z:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_bit_zp(self) -> None:
    """
    BIT - Bit Test, Zero Page.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_byte())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.flag_v = (self.read_byte(self.fetch_byte()) & 0x40) != 0
    self.cycles += 1

def ins_bit_abs(self) -> None:
    """
    BIT - Bit Test, Absolute.
    :return: None
    """
    self.reg_a = self.read_register_a() & self.read_byte(self.fetch_word())
    self.evaluate_flag_n(self.reg_a)
    self.evaluate_flag_z(self.reg_a)
    self.flag_v = (self.read_byte(self.fetch_word()) & 0x40) != 0
    self.cycles += 1

def ins_bmi_rel(self) -> None:
    """
    BMI - Branch if Minus.
    :return: None
    """
    if self.flag_n:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_bne_rel(self) -> None:
    """
    BNE - Branch if Not Equal.
    :return: None
    """
    if not self.flag_z:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_bpl_rel(self) -> None:
    """
    BPL - Branch if Positive.
    :return: None
    """
    if not self.flag_n:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_brk_imp(self) -> None:
    """
    BRK - Force Interrupt.
    :return: None
    """
    self.flag_b = True
    self.push((self.program_counter >> 8) & 0xFF)
    self.push(self.program_counter & 0xFF)
    self.push(self.flag_c)
    self.flag_i = True
    self.program_counter = self.read_word(0xFFFE)
    self.cycles += 1

def ins_bvc_rel(self) -> None:
    """
    BVC - Branch if Overflow Clear.
    :return: None
    """
    if not self.flag_v:
        self.program_counter += self.fetch_byte()
        self.cycles += 1

def ins_bvs_rel(self) -> None:
    """
    BVS - Branch if Overflow Set.
    :return: None
    """
    if self.flag_v:
        self.program_counter += self.fetch_byte()
        self.cycles += 1
