import glob

outlines = []

for script in glob.glob('scrape/*.txt'):
    lines = open(script).readlines()
    filtered_lines = []

    for line in lines[5:]:
        if line.strip() == '':
            continue
        if line.strip() == 'Bluey episode scripts':
            break

        # strip residual category headers
        if line.strip() == 'Episode' or line.strip() == 'Gallery' or line.strip() == 'Script':
            continue

        # remove TITLE CARD lines
        if line.find('TITLE') > -1:
            continue

        # remove in need of content warnings
        if line.find('This article/section is in need of content!') > -1:
            continue

        # remove icons
        if line.find('[[File:') > -1:
            continue
        
        # remove quotes, they are not consistent
        line = line.replace('"','')

        # if the line does not already start with a speaker, append Scene:
        if line.find(':') == -1:
            line = 'Scene: '+line 
        
        filtered_lines.append(line)

    if len(filtered_lines) < 16:
        print('SKIP', script, len(lines), len(filtered_lines))
        continue

    print(len(filtered_lines), script)
    outlines += filtered_lines

    #inject EOS token after every script
    outlines += ['<|endoftext|>\n']

with open('bluey.txt', 'w') as f:
    f.writelines(outlines)