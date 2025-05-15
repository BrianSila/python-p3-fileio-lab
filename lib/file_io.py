def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as text_file:
        text_file.write(append_content)
    pass

def read_file(file_name):
    with open(f"{file_name}.txt", mode="r", encoding="utf-8") as text_file:
        return text_file.read()