from lxml import etree
import glob
import json

folder='./data/'
regex='*.raw.xml'

filenames = glob.glob(folder+regex)

Q={}
L={}
T={}
B={}
N={}
A={}
TB={}

def getLabels(imageDiv,id):
    # print etree.tostring(image).strip()
    if not len(imageDiv) or not len(imageDiv[0]):
        return;
    imageA=imageDiv[0];
    image=imageA[0];
    url = image.get('src')
    name = image.get('alt')

    if url in L.keys():
        L[url]=L[url]+1;
    else:
        L[url]=1;

    if len(name):
        N[id]=name;
    return;

def joinText(fullText):
    body = '';
    c=1;
    if not fullText or len(fullText) == 0:
        return body;

    for div in fullText:
        if len(div):
            span=div[len(div)-1]
            text = span.text
            if text is not None:
                body+=' '+text.strip()
        c=c+1;
    # print body
    return body;



for filename in filenames:
    questionID = filename.replace(folder,'').replace(regex[1:],'').split('.')[0];
    if questionID in Q.keys():
        continue;
    # print questionID;
    parser = etree.XMLParser(recover=True);
    root = etree.parse(filename,parser);
    questionInfo = root.xpath('//div[@data-ya-question-id="'+questionID+'" and @role="main"]');

    for e in questionInfo:
        imageDiv = e.xpath('//div[@id="yq-question-detail-profile-img"]')[0];
        title = e.xpath('//h1[@itemprop="name"]')[0];
        titleText=title.text.strip();
        T[questionID]=titleText;
        getLabels(imageDiv,questionID);

        texts = e.xpath('//div[@class="Fz-13 Fw-n Mb-10" and span[@class="ya-q-text" or @class="ya-q-full-text"]]');
        body = joinText(texts);
        B[questionID]=body;
        TB[questionID]=titleText+' '+body;
    Q[questionID] = True;

with open('labelCount.txt', 'w+') as outfile:
    json.dump(L, outfile)
with open('title.txt', 'w+') as outfile:
    json.dump(T, outfile)
with open('body.txt', 'w+') as outfile:
    json.dump(B, outfile)
with open('titleBody.txt', 'w+') as outfile:
    json.dump(TB, outfile)
with open('avatars.txt', 'w+') as outfile:
    json.dump(A, outfile)
with open('names.txt', 'w+') as outfile:
    json.dump(N, outfile)
