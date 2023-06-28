import glob

outlines = []

skips = {'scrape/Rug Island.txt': 25,
         'scrape/Handstand.txt': -1}

for script in glob.glob('scrape/*.txt'):
    lines = open(script).readlines()
    filtered_lines = []
    skip_lines = skips.get(script, 5)

    if skip_lines == -1:
        continue

    for line in lines[skip_lines:]:
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
        if line.find('This article/section is in need of content!') > -1 or line.find('You can help by editing this section.') > -1:
            continue
        if line.strip().lower() == 'wip' or line.strip().lower() == 'work in progress':
            continue

        # remove icons
        if line.find('[[File:') > -1:
            continue
        
        # remove quotes, they are not consistent and trim trailing whitespace
        line = line.replace('"','').strip()

        # if the line does not already start with a speaker, append Scene:
        if line.find(':') == -1:
            line = 'Scene: '+line.replace('[]','')
        else:
            # strip whitespace around the speaker
            parts = line.split(':')
            if len(parts) > 2:
                parts = [ parts[0], ':'.join(parts[1:]) ]
            line = parts[0].strip()+': '+parts[1].strip()
        
        filtered_lines.append(line+'\n')

    if len(filtered_lines) < 16:
        print('SKIP', script, len(lines), len(filtered_lines))
        continue

    print(len(filtered_lines), script)
    outlines += filtered_lines

    #inject EOS token after every script
    outlines += ['<|endoftext|>\n']

with open('bluey.txt', 'w') as f:
    f.writelines(outlines)