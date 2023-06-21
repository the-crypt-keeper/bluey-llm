import glob

outlines = []

for script in glob.glob('*.txt'):
    lines = open(script).readlines()
    filtered_lines = []
    skip = False

    for line in lines[5:]:
        if line.strip() == '':
            continue
        if line.strip() == 'Bluey episode scripts':
            break
        #if 'This article/section is in need of content!' in line:
        #    skip = True
        #    break
        filtered_lines.append(line)

    if len(filtered_lines) < 20:
        print('SKIP', script, len(lines), len(filtered_lines))
        continue

    print(len(filtered_lines), script)
    outlines += filtered_lines

with open('bluey.txt', 'w') as f:
    f.writelines(outlines)