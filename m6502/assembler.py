OPCODES = [
    #       0       |       1       |       2       |       3       |       4       |       5       |       6       |       7       |       8       |       9       |       A       |       B       |       C       |       D       |       E       |       F       |
    ("imp", "brk"), ("inx", "ora"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zp" , "ora"), ("zp" , "asl"), ("   ", "   "), ("imp", "php"), ("imm", "ora"), ("acc", "asl"), ("   ", "   "), ("   ", "   "), ("abs", "ora"), ("abs", "asl"), ("   ", "   "),  # 0
    ("rel", "bpl"), ("iny", "ora"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zpx", "ora"), ("zpx", "asl"), ("   ", "   "), ("imp", "clc"), ("aby", "ora"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("abx", "ora"), ("abx", "asl"), ("   ", "   "),  # 1
    ("abs", "jsr"), ("inx", "and"), ("   ", "   "), ("   ", "   "), ("zp" , "bit"), ("zp" , "and"), ("zp" , "rol"), ("   ", "   "), ("imp", "plp"), ("imm", "and"), ("acc", "rol"), ("   ", "   "), ("abs", "bit"), ("abs", "and"), ("abs", "rol"), ("   ", "   "),  # 2
    ("rel", "bmi"), ("iny", "and"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zpx", "and"), ("zpx", "rol"), ("   ", "   "), ("imp", "sec"), ("aby", "and"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("abx", "and"), ("abx", "rol"), ("   ", "   "),  # 3
    ("imp", "rti"), ("inx", "eor"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zp" , "eor"), ("zp" , "lsr"), ("   ", "   "), ("imp", "pha"), ("imm", "eor"), ("acc", "lsr"), ("   ", "   "), ("abs", "jmp"), ("abs", "eor"), ("abs", "lsr"), ("   ", "   "),  # 4
    ("rel", "bvc"), ("iny", "eor"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zpx", "eor"), ("zpx", "lsr"), ("   ", "   "), ("imp", "cli"), ("aby", "eor"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("abx", "eor"), ("abx", "lsr"), ("   ", "   "),  # 5
    ("imp", "rts"), ("inx", "adc"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zp" , "adc"), ("zp" , "ror"), ("   ", "   "), ("imp", "pla"), ("imm", "adc"), ("acc", "ror"), ("   ", "   "), ("ind", "jmp"), ("abs", "adc"), ("abs", "ror"), ("   ", "   "),  # 6
    ("rel", "bvs"), ("iny", "adc"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zpx", "adc"), ("zpx", "ror"), ("   ", "   "), ("imp", "sei"), ("aby", "adc"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("abx", "adc"), ("abx", "ror"), ("   ", "   "),  # 7
    ("   ", "   "), ("inx", "sta"), ("   ", "   "), ("   ", "   "), ("zp" , "sty"), ("zp" , "sta"), ("zp" , "stx"), ("   ", "   "), ("imp", "dey"), ("   ", "   "), ("imp", "txa"), ("   ", "   "), ("abs", "sty"), ("abs", "sta"), ("abs", "stx"), ("   ", "   "),  # 8
    ("rel", "bcc"), ("iny", "sta"), ("   ", "   "), ("   ", "   "), ("zpx", "sty"), ("zpx", "sta"), ("zpy", "stx"), ("   ", "   "), ("imp", "tya"), ("aby", "sta"), ("imp", "txs"), ("   ", "   "), ("   ", "   "), ("abx", "sta"), ("   ", "   "), ("   ", "   "),  # 9
    ("imm", "ldy"), ("inx", "lda"), ("imm", "ldx"), ("   ", "   "), ("zp" , "ldy"), ("zp" , "lda"), ("zp" , "ldx"), ("   ", "   "), ("imp", "tay"), ("imm", "lda"), ("imp", "tax"), ("   ", "   "), ("abs", "ldy"), ("abs", "lda"), ("abs", "ldx"), ("   ", "   "),  # A
    ("rel", "bcs"), ("iny", "lda"), ("   ", "   "), ("   ", "   "), ("zpx", "ldy"), ("zpx", "lda"), ("zpy", "ldx"), ("   ", "   "), ("imp", "clv"), ("aby", "lda"), ("imp", "tsx"), ("   ", "   "), ("abx", "ldy"), ("abx", "lda"), ("aby", "ldx"), ("   ", "   "),  # B
    ("imm", "cpy"), ("inx", "cmp"), ("   ", "   "), ("   ", "   "), ("zp" , "cpy"), ("zp" , "cmp"), ("zp" , "dec"), ("   ", "   "), ("imp", "iny"), ("imm", "cmp"), ("imp", "dex"), ("   ", "   "), ("abs", "cpy"), ("abs", "cmp"), ("abs", "dec"), ("   ", "   "),  # C
    ("rel", "bne"), ("iny", "cmp"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zpx", "cmp"), ("zpx", "dec"), ("   ", "   "), ("imp", "cld"), ("aby", "cmp"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("abx", "cmp"), ("abx", "dec"), ("   ", "   "),  # D
    ("imm", "cpx"), ("inx", "sbc"), ("   ", "   "), ("   ", "   "), ("zp" , "cpx"), ("zp" , "sbc"), ("zp" , "inc"), ("   ", "   "), ("imp", "inx"), ("imm", "sbc"), ("imp", "nop"), ("   ", "   "), ("abs", "cpx"), ("abs", "sbc"), ("abs", "inc"), ("   ", "   "),  # E
    ("rel", "beq"), ("iny", "sbc"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("zpx", "sbc"), ("zpx", "inc"), ("   ", "   "), ("imp", "sed"), ("aby", "sbc"), ("   ", "   "), ("   ", "   "), ("   ", "   "), ("abx", "sbc"), ("abx", "inc"), ("   ", "   "),  # F
]
OPCODE_NAMES = [i[1] for i in OPCODES]

BYTEORDER = "little"


from enum import Enum
class ParserState(Enum):
    NONE           = 0
    ALNUM          = 1
    HASHTAG        = 2
    DOLLAR         = 3
    HASHTAG_DOLLAR = 4

class Token:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.__class__.__name__.removesuffix("Token") + (("{"+str(self.value)+"}") if self.value != None else "")

class NewlineToken(Token):
    def __init__(self): super().__init__(value=None)

class AlnumToken(Token):
    def __init__(self, value): super().__init__(value=value)

class ImmediateOperandToken(Token):
    def __init__(self, value): super().__init__(value=value)

class AddressOperandToken(Token):
    def __init__(self, value): super().__init__(value=value)

class OpeningBracketToken(Token):
    def __init__(self): super().__init__(value=None)

class ClosingBracketToken(Token):
    def __init__(self): super().__init__(value=None)

class LabelReference:
    def __init__(self, name: str, is_word: bool):
        self.name = name
        self.is_word = is_word
    def __repr__(self):
        return f"LabelReference[{'W' if self.is_word else 'B'}]({self.name})"

string = """
START   LDA #$10   ; 'START' is a label pointing to this line
LOOP    STA $0200  ; 'LOOP' is another label
        JMP LOOP   ; JMP will jump to 'LOOP'
        LDA ($20,X)
        LDA ($20),Y
"""

lines = string.splitlines()
code = ""
for line in lines:
    if ";" in line:
        line = line[:line.index(";")]
    line = line.strip()
    if line == "": continue
    if code != "":
        code += "\n"
    code += line

def endToken():
    global state, token_chars
    if   state == ParserState.NONE: pass
    elif state == ParserState.ALNUM:
        if token_chars != "":
            tokens.append(AlnumToken(token_chars))
            token_chars = ""
            state = ParserState.NONE
    elif state == ParserState.DOLLAR:
        if token_chars != "":
            value = int("0x" + token_chars, base=16)
            tokens.append(AddressOperandToken(value))
            token_chars = ""
            state = ParserState.NONE
    elif state == ParserState.HASHTAG_DOLLAR:
        if token_chars != "":
            value = int("0x" + token_chars, base=16)
            tokens.append(ImmediateOperandToken(value))
            token_chars = ""
            state = ParserState.NONE
    else: raise Exception(state)

lines = code.splitlines()
token_chars = ""
state = ParserState.NONE
tokens = []
for line in lines:
    for char in line:
        if char in {" ", ","}:
            endToken()
        
        elif char == "#":
            if   state == ParserState.NONE:
                state = ParserState.HASHTAG
            else: raise Exception(state)
        
        elif char == "$":
            if   state == ParserState.NONE:
                state = ParserState.DOLLAR
            elif state == ParserState.HASHTAG:
                state = ParserState.HASHTAG_DOLLAR
            else: raise Exception(state)
        
        elif char == "(":
            if   state == ParserState.NONE:
                tokens.append(OpeningBracketToken())
            else: raise Exception(state)
        elif char == ")":
            endToken()
            if   state == ParserState.NONE:
                tokens.append(ClosingBracketToken())
            else: raise Exception(state)

        elif char.isalnum():
            if   state == ParserState.NONE:
                state = ParserState.ALNUM
            elif state == ParserState.ALNUM: pass
            elif state == ParserState.DOLLAR: pass
            elif state == ParserState.HASHTAG_DOLLAR: pass
            else: raise Exception(state)

            if state in {ParserState.ALNUM, ParserState.DOLLAR, ParserState.HASHTAG_DOLLAR}:
                token_chars += char
        
        else: raise Exception(repr(char))
        print(repr(char), state)
    endToken()
    tokens.append(NewlineToken())
print(code)
print("one", tokens)


ordered_tokens = []
line_tokens = []
for token in tokens:
    if isinstance(token, NewlineToken):
        if line_tokens != []:
            ordered_tokens.append(line_tokens)
        line_tokens = []
    else:
        line_tokens.append(token)
print("ordered", ordered_tokens)

bytes = []
label_addresses = {}
for line_tokens in ordered_tokens:
    assert len(line_tokens) >= 1
    first_token  = line_tokens[0] if (0 in range(len(line_tokens))) else None
    second_token = line_tokens[1] if (1 in range(len(line_tokens))) else None
    first_token_value  = None if (first_token  is None) else first_token.value
    second_token_value = None if (second_token is None) else second_token.value
    if not isinstance(first_token, AlnumToken): raise Exception()
    
    assert isinstance(first_token, AlnumToken)
    if isinstance(second_token, AlnumToken) and (second_token_value is not None) and (second_token_value.lower() in OPCODE_NAMES):
        label       = first_token_value
        opcode_name = second_token_value.lower()
        remaining_tokens = line_tokens[2:]
    else:
        label       = None
        opcode_name = first_token_value.lower()
        remaining_tokens = line_tokens[1:]
    first_token  = remaining_tokens[0] if (0 in range(len(remaining_tokens))) else None
    second_token = remaining_tokens[1] if (1 in range(len(remaining_tokens))) else None
    third_token  = remaining_tokens[2] if (2 in range(len(remaining_tokens))) else None
    fourth_token = remaining_tokens[3] if (3 in range(len(remaining_tokens))) else None
    first_token_value  = None if (first_token  is None) else first_token.value
    second_token_value = None if (second_token is None) else second_token.value
    third_token_value  = None if (third_token  is None) else third_token.value
    fourth_token_value = None if (fourth_token is None) else fourth_token.value
    
    if   (isinstance(first_token, OpeningBracketToken) and isinstance(second_token, AddressOperandToken)
                and (third_token_value == "X")         and isinstance(fourth_token, ClosingBracketToken)):
        addressing_mode = "inx"
        operand         = second_token_value
        operand_bits    = 8
    elif (isinstance(first_token, OpeningBracketToken) and isinstance(second_token, AddressOperandToken)
      and isinstance(third_token, ClosingBracketToken) and (fourth_token_value == "Y")):
        addressing_mode = "iny"
        operand         = second_token_value
        operand_bits    = 8
    elif (isinstance(first_token, OpeningBracketToken) and isinstance(second_token, AddressOperandToken)
      and isinstance(third_token, ClosingBracketToken) and (fourth_token is None)):
        addressing_mode = "ind"
        operand         = second_token_value
        operand_bits    = 16
    elif (third_token is None) and (fourth_token is None):
        if (first_token is None) and (second_token is None):
            addressing_mode = "imp"
            operand         = None
            operand_bits    = None 
        elif isinstance(first_token, ImmediateOperandToken) and (second_token is None):
            addressing_mode = "imm"
            operand         = first_token_value
            operand_bits    = 8
        elif isinstance(first_token, AddressOperandToken) and (second_token is None):
            if first_token_value < 0x100: addressing_mode, operand_bits = "zp" , 8 
            else                        : addressing_mode, operand_bits = "abs", 16
            operand = first_token_value
        elif isinstance(first_token, AddressOperandToken) and (second_token_value == "X"):
            if first_token_value < 0x100: addressing_mode, operand_bits  = "zpx", 8 
            else                        : addressing_mode, operand_bits  = "abx", 16
            operand = first_token_value
        elif isinstance(first_token, AddressOperandToken) and (second_token_value == "Y"):
            if first_token_value < 0x100: addressing_mode, operand_bits  = "zpy", 8 
            else                        : addressing_mode, operand_bits  = "aby", 16
            operand = first_token
        elif (first_token_value == "A") and (second_token is None):
            addressing_mode = "acc"
            operand         = None
            operand_bits    = None
        elif isinstance(first_token, AlnumToken) and (second_token is None):
            if opcode_name in {"jmp", "jsr"}:
                addressing_mode = "abs"
                operand         = LabelReference(first_token_value, is_word=True )
                operand_bits    = 16
            else:
                addressing_mode = "rel"
                operand         = LabelReference(first_token_value, is_word=False)
                operand_bits    = 8
        else: raise Exception()
    else: raise Exception()
    id = (addressing_mode, opcode_name)
    if id not in OPCODES: raise Exception(id)
    
    instr_bytes = []
    opcode_num = OPCODES.index(id)
    instr_bytes.append(opcode_num)
    if isinstance(operand, int):
        if operand_bits == 8:
            if (operand >= 0xFF) or (operand < -0x80): raise ValueError()
            instr_bytes.append(operand)
        elif operand_bits == 16:
            if (operand >= 0xFFFF) or (operand < -0x8000): raise ValueError()
            if BYTEORDER == "little":
                instr_bytes.append((operand >> 0) & 0xFF)
                instr_bytes.append((operand >> 8) & 0xFF)
            else:
                instr_bytes.append((operand >> 8) & 0xFF)
                instr_bytes.append((operand >> 0) & 0xFF)
        else: raise Exception()
    elif isinstance(operand, LabelReference):
        instr_bytes.append(operand)
    elif operand is None: pass
    else: raise Exception()
    if label is not None:
        label_addresses[label] = len(bytes)
    bytes += instr_bytes
    print(label, instr_bytes)

print(bytes, label_addresses)
final_bytes = []
for i, item in enumerate(bytes):
    if isinstance(item, LabelReference):
        address = label_addresses[item.name]
        if item.is_word:
            if (operand >= 0xFFFF) or (operand < -0x8000): raise ValueError()
            if BYTEORDER == "little":
                final_bytes.append((address >> 0) & 0xFF)
                final_bytes.append((address >> 8) & 0xFF)
            else:
                final_bytes.append((address >> 8) & 0xFF)
                final_bytes.append((address >> 0) & 0xFF)
        else:
            if (operand >= 0xFF) or (operand < -0x80): raise ValueError()
            final_bytes.append(address)
    else:
        final_bytes.append(item)
print(final_bytes, label_addresses)
