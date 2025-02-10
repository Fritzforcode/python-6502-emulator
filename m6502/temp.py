from main import *
def P_ins_sbc_imm(self: dict) -> None:
    """
    SBC - Subtract with Carry, Immediate.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, operand = P_fetch_byte(self)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_zp(self: dict) -> None:
    """
    SBC - Subtract with Carry, Zero Page.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, address = P_fetch_byte(self)
    self, operand = P_read_byte(self, address)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_zpx(self: dict) -> None:
    """
    SBC - Subtract with Carry, Zero Page, X.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, base_address = P_fetch_byte(self)
    self, address_offset = P_read_register_x(self)
    self, operand = P_read_byte(self, (base_address + address_offset) & 0xFF)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_abs(self: dict) -> None:
    """
    SBC - Subtract with Carry, Absolute.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, address = P_fetch_word(self)
    self, operand = P_read_byte(self, address)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_abx(self: dict) -> None:
    """
    SBC - Subtract with Carry, Absolute, X.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, base_address = P_fetch_word(self)
    self, address_offset = P_read_register_x(self)
    self, operand = P_read_byte(self, base_address + address_offset)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_aby(self: dict) -> None:
    """
    SBC - Subtract with Carry, Absolute, Y.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, base_address = P_fetch_word(self)
    self, address_offset = P_read_register_y(self)
    self, operand = P_read_byte(self, base_address + address_offset)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_inx(self: dict) -> None:
    """
    SBC - Subtract with Carry, Indexed Indirect.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, base_address = P_fetch_byte(self)
    self, address_offset = P_read_register_x(self)
    self, operand = P_read_byte(self, base_address + address_offset)
    self["reg_a"] = old_value + operand
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1

def P_ins_sbc_iny(self: dict) -> None:
    """
    SBC - Subtract with Carry, Indirect Indexed.
    :return: None
    """
    self, old_value = P_read_register_a(self)
    self, address = P_fetch_byte(self)
    self, read_byte = P_read_byte(self, address)
    self, operand_offset = P_read_register_y(self)
    self["reg_a"] = old_value + read_byte + operand_offset
    self, _ = P_evaluate_flags_nz_a(self)
    self["cycles"] += 1
