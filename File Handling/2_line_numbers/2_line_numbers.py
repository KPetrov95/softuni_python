from string import punctuation

with open("text.txt", "r")as initial_f, open("output.txt", "w") as output_f:
    edited_lines = []
    for row_index, line in enumerate(initial_f):
        letters_count = 0
        punctuation_count = 0
        for el in line:
            if el.isalpha():
                letters_count += 1
            elif el in punctuation:
                punctuation_count += 1
        edited_lines.append(f"Line {row_index + 1}: {line.strip()} ({letters_count})({punctuation_count})")
    output_f.write(f"\n".join(edited_lines))
