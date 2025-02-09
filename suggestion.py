def P_ins_adc_imm(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Immediate.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self["reg_a"] = t1 ^ t2
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_zp(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Zero Page.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 ^ t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_zpx(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Zero Page, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, (t2 + t3) & 0xFF)
    self["reg_a"] = t1 ^ t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_abs(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Absolute.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_byte(self, t2)
    self["reg_a"] = t1 ^ t3
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_abx(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Absolute, X.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 ^ t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_aby(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Absolute, Y.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_word(self)
    self, t3 = P_read_register_y(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 ^ t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_inx(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Indexed Indirect.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_register_x(self)
    self, t4 = P_read_byte(self, t2 + t3)
    self["reg_a"] = t1 ^ t4
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1

def P_ins_adc_iny(self: dict) -> None:
    """
    EOR - XOR of Memory with Accumulator, Indirect Indexed.
    :return: None
    """
    self, t1 = P_read_register_a(self)
    self, t2 = P_fetch_byte(self)
    self, t3 = P_read_byte(self, t2)
    self, t4 = P_read_register_y(self)
    self["reg_a"] = t1 ^ t3 + t4
    self.reg_a = self.read_register_a() + self.read_byte(self.fetch_byte()) + self.read_register_y()
    self, _ = P_evaluate_flag_n(self, self["reg_a"])
    self, _ = P_evaluate_flag_z(self, self["reg_a"])
    self["cycles"] += 1
