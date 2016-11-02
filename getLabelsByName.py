
from collections import OrderedDict

wordsByGender = {}

fnames = ['female', 'male']

for x in fnames:
    wordsByGender[x]=[]
    with open('{}Words.txt'.format(x), 'r') as inputFile:
        lines = inputFile.readlines();
        for i, line in enumerate(lines):
            wordsByGender[x].append(line.strip());
    print wordsByGender[x]

print 'wordsByGender: '
print wordsByGender
print '\n '

with open('namesVector.txt'.format(x), 'r') as f:
    lines = f.readlines();
    tags = []
    tagsAndName = []
    for i, line in enumerate(lines):
        name = line.lower();
        words = name.split()
        text = '0';
        for word in words:
            if word in wordsByGender['female']:
                text+='-1';
            if word in wordsByGender['male']:
                text+='+1';
        value=eval(text)
        tag = ''
        if value>0:
            tag='1';
        if value<0:
            tag='-1';
        if value==0:
            tag='0';
        tags.append(tag);
        tagsAndName.append(tag+': '+name)
    with open('tags.txt'.format(x), 'w+') as of:
        for tag in tags:
            of.write(tag+'\n');
    with open('tagAndNames.txt'.format(x), 'w+') as of:
        for tagAndName in tagsAndName:
            of.write(tagAndName)
