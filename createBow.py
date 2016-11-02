from collections import Counter
import collections, re

folder='./oldRuns/'
sources = ['title','body','titleBody']
bagofwords=[]

for source in sources:
	with open(folder+'{}.txt'.format(source), 'r') as f:
		lines = f.readlines();
    	for line in enumerate(lines):
    		print line
    		words = collections.Counter(re.findall(r'\w+', text.lower()))
    		bagofwords.append(words)

    	sumbags = sum(bagsofwords, collections.Counter())
	    mostCommon = sumbags.most_common()
	    # print 'Dimensions: {}'.format(len(sumbags))
	    # print 'Sumbags: {}'.format(sumbags)
	    print 'Most common: {}'.format(mostCommon)

	    with open(source+'BOW.txt','w+') as bagFile:
	    	for word,count in mostCommon:
	        	bagFile.write('{}:{}\n'.format(word,count))
  
	    with open(source+'SVM.txt','w+') as completefile:
	        for v in enumerate(bagsofwords):
	            dic=dict(v)
	            # print 'dic: {}'.format(dic)
	            # print 'class: {}'.format(classes[i])
	            fileLine=''
	            for index, (word,count) in enumerate(mostCommon):
	                # print 'index: {}'.format(index)
	                # print 'word: {}'.format(word)
	                # print 'count: {}'.format(count)

	                if dic.get(word) > 0:
	                    feat = '{}:{} '.format(index+1,dic[word])
	                    fileLine+=feat
	            completefile.write(fileLine+'\n')
