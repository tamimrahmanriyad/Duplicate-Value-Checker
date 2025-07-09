import re
import os
from collections import defaultdict

def find_first_txt_file():
    for file in os.listdir():
        if file.endswith('.txt') and file.lower() != 'output.txt':
            return file
    return None

def find_duplicate_pins_in_file():
    file_path = find_first_txt_file()
    if not file_path:
        return "No .txt file found in the current directory (excluding output.txt)."

    pin_lines = defaultdict(list)
    pin_pattern = re.compile(r'"pin"\s*:\s*"(\d+)"')

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            match = pin_pattern.search(line)
            if match:
                pin = match.group(1)
                pin_lines[pin].append(line_number)

    output_lines = []
    for pin, lines in pin_lines.items():
        if len(lines) > 1:
            output_lines.append(f"Duplicate PIN {pin} found on lines: {lines}")

    if not output_lines:
        return "No duplicate PINs found."
    
    return "\n".join(output_lines)

if __name__ == "__main__":
    result = find_duplicate_pins_in_file()
    with open("output.txt", "w", encoding="utf-8") as out_file:
        out_file.write(result + "\n")
