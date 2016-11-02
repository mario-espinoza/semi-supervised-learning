from collections import Counter
import collections, re, io

folder='./output/'
sources = ['title','body','titleBody']
processedWords = []

for source in sources:
	print 'read text {}'.format(source);
	bag = []
	with io.open('{}{}.txt'.format(folder,source),'r',encoding='utf-8') as f:
		lines=f.readlines();
		for line in lines:
			line=' '.join(line.encode('utf-8').lower().split());
			line=line.replace('\n','');
			words = re.findall(r'\w+', line)
			processedWords.append(words)
			for word in words:
				if  len(word) and word not in bag:
					bag.append(word)
					
	print 'writing BOW';
	with open('{}Bow.txt'.format(source),'w+') as bagFile:
		for word in bag:
			bagFile.write('{}\n'.format(word));
	print 'writing Vector';
	
	with open('{}SVM.txt'.format(source),'w+') as completefile:
		for wordsInLine in processedWords:
			fileLine='';
			for index, word in enumerate(bag):
				count = wordsInLine.count(word)
				if count:
					feat = '{}:{} '.format(index+1,count);
					fileLine+=feat;
			completefile.write(fileLine.strip()+'\n');
