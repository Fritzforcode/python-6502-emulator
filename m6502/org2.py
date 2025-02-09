def ins_cmp_imm(self) -> None:
    """
    CMP - Compare, Immediate.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.fetch_byte())
    self.evaluate_flag_z(self.read_register_a() - self.fetch_byte())
    self.cycles += 1

def ins_cmp_zp(self) -> None:
    """
    CMP - Compare, Zero Page.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte(self.fetch_byte()))
    self.evaluate_flag_z(self.read_register_a() - self.read_byte(self.fetch_byte()))
    self.cycles += 1

def ins_cmp_zpx(self) -> None:
    """
    CMP - Compare, Zero Page, X.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte((self.fetch_byte() + self.read_register_x()) & 0xFF))
    self.evaluate_flag_z(self.read_register_a() - self.read_byte((self.fetch_byte() + self.read_register_x()) & 0xFF))
    self.cycles += 1

def ins_cmp_abs(self) -> None:
    """
    CMP - Compare, Absolute.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte(self.fetch_word()))
    self.evaluate_flag_z(self.read_register_a() - self.read_byte(self.fetch_word()))
    self.cycles += 1

def ins_cmp_abx(self) -> None:
    """
    CMP - Compare, Absolute, X.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte(self.fetch_word() + self.read_register_x()))
    self.evaluate_flag_z(self.read_register_a() - self.read_byte(self.fetch_word() + self.read_register_x()))
    self.cycles += 1

def ins_cmp_aby(self) -> None:
    """
    CMP - Compare, Absolute, Y.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte(self.fetch_word() + self.read_register_y()))
    self.evaluate_flag_z(self.read_register_a() - self.read_byte(self.fetch_word() + self.read_register_y()))
    self.cycles += 1

def ins_cmp_inx(self) -> None:
    """
    CMP - Compare, Indexed Indirect.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte(self.fetch_byte() + self.read_register_x()))
    self.evaluate_flag_z(self.read_register_a() - self.read_byte(self.fetch_byte() + self.read_register_x()))
    self.cycles += 1

def ins_cmp_iny(self) -> None:
    """
    CMP - Compare, Indirect Indexed.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_a() - self.read_byte(self.fetch_byte()) + self.read_register_y())
    self.evaluate_flag_z(self.read_register_a() - self.read_byte(self.fetch_byte()) + self.read_register_y())
    self.cycles += 1

def ins_cpx_imm(self) -> None:
    """
    CPX - Compare X Register, Immediate.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_x() - self.fetch_byte())
    self.evaluate_flag_z(self.read_register_x() - self.fetch_byte())
    self.cycles += 1

def ins_cpx_zp(self) -> None:
    """
    CPX - Compare X Register, Zero Page.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_x() - self.read_byte(self.fetch_byte()))
    self.evaluate_flag_z(self.read_register_x() - self.read_byte(self.fetch_byte()))
    self.cycles += 1

def ins_cpx_abs(self) -> None:
    """
    CPX - Compare X Register, Absolute.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_x() - self.read_byte(self.fetch_word()))
    self.evaluate_flag_z(self.read_register_x() - self.read_byte(self.fetch_word()))
    self.cycles += 1

def ins_cpy_imm(self) -> None:
    """
    CPY - Compare Y Register, Immediate.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_y() - self.fetch_byte())
    self.evaluate_flag_z(self.read_register_y() - self.fetch_byte())
    self.cycles += 1

def ins_cpy_zp(self) -> None:
    """
    CPY - Compare Y Register, Zero Page.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_y() - self.read_byte(self.fetch_byte()))
    self.evaluate_flag_z(self.read_register_y() - self.read_byte(self.fetch_byte()))
    self.cycles += 1

def ins_cpy_abs(self) -> None:
    """
    CPY - Compare Y Register, Absolute.
    :return: None
    """
    self.evaluate_flag_n(self.read_register_y() - self.read_byte(self.fetch_word()))
    self.evaluate_flag_z(self.read_register_y() - self.read_byte(self.fetch_word()))
    self.cycles += 1
