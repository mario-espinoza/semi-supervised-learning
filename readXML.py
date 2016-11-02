from lxml import etree
import glob, json

folder='./data/'
outputFolder='./output/'
regex='*.raw.xml'

filenames = glob.glob(folder+regex)
attributes = ['title','body','titleBody','avatars','names']

Q={}
DATA={}

for attrib in attributes:
    DATA[attrib]={}

def getLabels(imageDiv,id):
    if not len(imageDiv) or not len(imageDiv[0]):
        DATA['names'][id]='_';
        return;
    image=imageDiv[0][0];

    url = image.get('src')
    name = image.get('alt')

    if url in L.keys():
        DATA['avatars'][url]=L[url]+1;
    else:
        DATA['avatars'][url]=1;

    if len(name):
        DATA['names'][id]=name.lower().encode('utf-8');
    else:
        DATA['names'][id]='_';
        print '_';
    return;

def joinText(fullText):
    body = '';
    if not fullText or len(fullText) == 0:
        return body;

    for div in fullText:
        if len(div):
            span=div[len(div)-1]
            text = span.text
            if text is not None:
                body+=' '+' '.join(text.lower().split())
    return body;

count = 0
for filename in filenames:
    questionID = filename.replace(folder,'').replace(regex[1:],'').split('.')[0];

    if questionID in Q.keys():
        continue;

    parser = etree.XMLParser(encoding='utf-8',recover=True);
    root = etree.parse(filename,parser);
    questionInfo = root.xpath('//div[@data-ya-question-id="'+questionID+'" and @role="main"]');

    for e in questionInfo:
        imageDiv = e.xpath('//div[@id="yq-question-detail-profile-img"]')[0];
        title = e.xpath('//h1[@itemprop="name"]')[0];
        titleText=' '.join(title.text.lower().split()).encode('utf-8');
        DATA['title'][questionID]=titleText;
        getLabels(imageDiv,questionID);
        texts = e.xpath('//div[@class="Fz-13 Fw-n Mb-10" and span[@class="ya-q-text" or @class="ya-q-full-text"]]');
        body = joinText(texts).encode('utf-8').strip();
        DATA['body'][questionID]=body;
        DATA['titleBody'][questionID]=titleText+' '+body;
    Q[questionID] = True;
    count+=1
print count

for attrib in attributes:
    data = DATA[attrib];
    with open('{}.txt'.format(attrib), 'w+') as outfile:
        json.dump(data, outfile, ensure_ascii=False);
    with open('{}Vector.txt'.format(attrib), 'w+') as outfile:
        for d in data.keys():
            outfile.write(str(data[d])+'\n');

