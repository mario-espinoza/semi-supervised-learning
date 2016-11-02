from collections import Counter
import collections, re

folder='./output/'
sources = ['title','body','titleBody']
bagOfWords=[]


for source in sources:
	print 'read text {}'.format(source);
	with open(folder+'{}.txt'.format(source), 'r') as f:
		lines = f.readlines();
		for i,line in enumerate(lines):
			words = collections.Counter(re.findall(r'\w+', line.strip().lower()));
			bagOfWords.append(words);
	print 'here'
	sumbags = sum(bagOfWords, collections.Counter());
	mostCommon = sumbags.most_common();

	print 'writing BOW';
	with open('{}BOW.txt'.format(source),'w+') as bagFile:
		for word,count in mostCommon:
			bagFile.write('{}:{}\n'.format(word,count));
	print 'writing Vector';
	with open('{}SVM.txt'.format(source),'w+') as completefile:
		for v in enumerate(bagOfWords):
			dic=dict(v);
			fileLine='';
			for index, (word,count) in enumerate(mostCommon):
				if dic.get(word) > 0:
					feat = '{}:{} '.format(index+1,dic[word]);
					fileLine+=feat;
			completefile.write(fileLine+'\n');
