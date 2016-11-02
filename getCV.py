import os
total=116692
headSize=29173;
R='0.65';
tailSize=total-headSize;
folder='./'
svmlinFolder='../svmlin/'
labelsFolder='./'
dataSources=['title']
#,'body','titleBody']
getLabelTrainingFiles='head -n {} {}tags.txt >> labels_train.txt'.format(headSize,labelsFolder);
getLabelTestFiles='tail -n {} {}tags.txt >> labels_test.txt'.format(tailSize,labelsFolder);
os.system(getLabelTrainingFiles);
os.system(getLabelTestFiles);
for source in dataSources:
	getTrainingFiles='head -n {} ./{}SVM.txt >> {}_train.txt'.format(headSize,source,source);
	getTestFiles='tail -n {} {}SVM.txt >> {}_test.txt'.format(tailSize,source,source);
	
	os.system(getTrainingFiles);
	os.system(getTestFiles);
	
	train='{}svmlin -A 2 -W 0.001 -U 1 -R {} {}_train.txt labels_train.txt >> trainRun_{}.txt'.format(svmlinFolder,R,source,source);
	test='{}svmlin -f  {}_train.weights {}_test.txt abels_test'.format(svmlinFolder,source,source);
	os.system(train);
	os.system(test);