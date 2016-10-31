from lxml import etree
import glob

folder='./test/'
regex='*.raw.xml'

filenames = glob.glob(folder+regex)

def getProfileData(image):
    # print etree.tostring(image).strip()
    return;

def joinText(fullText):
    body = '';
    c=1;
    if not fullText or len(fullText) == 0:
        return body;

    print 'fullText: '
    print fullText
    print '\n'
    for elem in fullText:
        print 'text {}:'.format(c)
        # print etree.tostring(elem)
        if len(elem):

            text = etree.tostring(elem)
            cleanText= text.strip().replace('<br/>','');
            print text
            # print cleanText
        c=c+1
    return body;

titleFile = output = open('title.txt', 'w+');
titleBodyFile = output = open('titleBody.txt', 'w+');

Q={}
j=1
for filename in filenames:
    questionID = filename.replace(folder,'').replace(regex[1:],'').split('.')[0]

    # /questionID = '20160731071028AABlBsc'

    if questionID in Q.keys():
        continue

    print questionID
    parser = etree.XMLParser(recover=True)
    root = etree.parse(filename,parser)
    questionInfo = root.xpath('//div[@data-ya-question-id="'+questionID+'" and @role="main"]')

    i=1
    for e in questionInfo:
        print 'Element {}.{}'.format(j,i)
        image = e.xpath('//div[@id="yq-question-detail-profile-img"]')[0]
        title = e.xpath('//h1[@itemprop="name"]')[0]

        print 'title: ' + title.text.strip()


        getProfileData(image)

        texts = e.xpath('//div[@class="Fz-13 Fw-n Mb-10" and ./span[@class="ya-q-text" or @class="ya-q-full-text"]]')
        body = joinText(texts);

        # print etree.tostring(t)
        print '\n'
        i=i+1
    j=j+1
    Q[questionID] = True;
