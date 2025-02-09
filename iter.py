import os, ast

flag_texts = ["|  C   | Carry Flag        |", "|  Z   | Zero Flag         |", "|  I   | Interrupt Disable |", "|  D   | Decimal Mode Flag |", "|  B   | Break Command     |", "|  V   | Overflow Flag     |", "|  N   | Negative Flag     |"]

string = ""
ghu = "+------+-------------------+--------------+"

for name in os.listdir("tests"):
    #if name in ["__init__.py", "test_cpu.py", "test_memory.py"]: continue
    if not name.startswith("test_cpu_ins"): continue
    path = os.path.join("tests", name)
    print("-", name, path)
    with open(path, "r") as file:
        code = file.read()
    tree = ast.parse(code)
    comment = tree.body[0].value.value
    comment_lines = []
    for line in comment.splitlines():
        if not "|" in line:
            keep = True
            if "---" in line:
                if line == comment_lines[-1]:
                    keep = False
            if keep:
                comment_lines.append(line)
            continue
        keep = True
        for flag_text in flag_texts:
            if line.startswith(flag_text) and ("Not affected" in line):
                keep = False
                continue
        if keep and "---" in line:
            if line == comment_lines[-1]:
                keep = False
        if keep:
            comment_lines.append(line)
    string += f"================== {name} ==================\n"
    string += "\n".join(comment_lines) + 3*"\n"
    #print(ast.dump(comment, indent=4))
print(string)
