# -*- coding:utf-8 -*-import requestsfrom bs4 import BeautifulSoupimport sysclass Joke:    def __init__(self):        self.basURL='http://www.qiushibaike.com/hot/page/'    def getPage(self,pageIndex):        getURL = self.basURL+str(pageIndex)+'/?s=4945642'        response = requests.get(getURL).text        print u'正在加载第%s页内容' %(pageIndex)        return response    def getItem(self,pageIndex):        content = self.getPage(pageIndex)        soup = BeautifulSoup(content,'lxml')        print u'返回第%s页内容' %(pageIndex)        items = []        for i in soup.select('.content'):            items.append(i.text)        return items    def saveJoke(self,items):        reload(sys)        sys.setdefaultencoding('utf-8')        with open('joke.txt','w+') as f:            for b in items:                f.write(b)        print u'保存成功'    def main(self,num):        items = []        for i in range(num):            item = self.getItem(i+1)            items=items+item        self.saveJoke(items)spyder = Joke()spyder.main(20)