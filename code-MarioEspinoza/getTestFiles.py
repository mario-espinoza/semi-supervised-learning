import io

folder='./'
sources = ['title']
# ,'body','titleBody']
with open('new_labels_test.txt', 'w+') as lof:
	with open('labels_testing.txt', 'r') as lf:
		labels=lf.readlines();
		for source in sources:
			f=open('{}{}SVM.txt'.format(folder,source), 'r')
			lines=f.readlines();
			of=open('new_{}_test.txt'.format(source), 'w+');
			for i,label in enumerate(labels):
				label=label.strip()
				if label is not '0':
					of.write(lines[i])
					lof.write(label+'\n')
			of.close
			f.close