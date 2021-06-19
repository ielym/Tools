#coding:utf-8
from PyPDF2 import PdfFileReader,PdfFileWriter
import os
import sys
import time
class sumaryPDFs:
    def __init__(self):
        self.outer = PdfFileWriter()

        self.get_file_page()

        self.makeNewPDF()



    def get_file_page(self):
        pdffiles = self.getPDFfilenames()
        for apdfFile in pdffiles:
            contents = PdfFileReader(open(os.path.join('./pdfs', apdfFile), 'rb'))
            total_pages = contents.getNumPages()
            pageStr = input('请输入合并 {} 文件中的第几页，总共{}页（输入all表示合并所有页，2-8表示合并部分页）：'.format(apdfFile, total_pages))
            #=============================================================================================================
            if pageStr == 'all':
                self.allPage(contents, total_pages)
            # =============================================================================================================
            elif '-' in pageStr:
                startPage, endPage = pageStr.split('-')
                try:
                    #===================================检查起始页数
                    startPage = int(startPage)
                    if startPage > total_pages:
                        print('错误：输入的页数大于总页数！！！')
                        time.sleep(3)
                        sys.exit(-1)
                    if startPage < 1:
                        print('错误：输入的页数小于1！！！')
                        time.sleep(3)
                        sys.exit(-1)

                    # ===================================检查截止页数
                    endPage = int(endPage)
                    if endPage > total_pages:
                        print('错误：输入的页数大于总页数！！！')
                        time.sleep(3)
                        sys.exit(-1)
                    if endPage < 1:
                        print('错误：输入的页数小于1！！！')
                        time.sleep(3)
                        sys.exit(-1)
                    if startPage > endPage:
                        print('错误：截止页数小于开始页数！！！')
                        time.sleep(3)
                        sys.exit(-1)
                    self.partPage(contents, startPage-1, endPage)

                except Exception as e:
                    print(e)
                    print('错误：请输入合法的数字！！！')
                    time.sleep(3)
                    sys.exit(-1)

                print(startPage, endPage)
            # =============================================================================================================
            else:
                try:
                    intPage = int(pageStr)
                    if intPage > total_pages:
                        print('错误：输入的页数大于总页数！！！')
                        time.sleep(3)
                        sys.exit(-1)
                    if intPage < 1:
                        print('错误：输入的页数小于1！！！')
                        time.sleep(3)
                        sys.exit(-1)
                    self.aPage(contents, intPage-1)
                except Exception as e:
                    print(e)
                    print('错误：请输入合法的数字！！！')
                    time.sleep(3)
                    sys.exit(-1)


    def getPDFfilenames(self):
        if not os.path.exists('./pdfs'):
            print('错误：请将所有PDF文件放在当前目录的pdfs文件夹下!!!')
            time.sleep(3)
            sys.exit(-1)
        pdffiles = os.listdir('./pdfs')
        totalPDFfiles = []
        for afile in pdffiles:
            if afile.endswith('.pdf'):
                totalPDFfiles.append(afile)
        if len(totalPDFfiles) <= 0:
            print('错误：请检查pdfs文件夹下是否存在PDF格式文件!!!')
            time.sleep(3)
            sys.exit(-1)
        if len(totalPDFfiles) > 2:
            print('错误：每次最多只支持合并2个PDF文件，解锁新功能请联系ieluoyiming@163.com!!!')
            time.sleep(5)
            sys.exit(-1)
        return totalPDFfiles

    def allPage(self, contents, total_pages):
        for page in range(total_pages):
            self.outer.addPage(contents.getPage(page))
    def partPage(self, contents, startpage, endpage):
        for page in range(startpage, endpage):
            self.outer.addPage(contents.getPage(page))

    def aPage(self, contents, page):
        self.outer.addPage(contents.getPage(page))

    def makeNewPDF(self):

        newfilename = input('请输入合并文件的文件名')
        self.outer.write(open(os.path.join('./', '{}.pdf'.format(newfilename)), 'wb'))

if __name__ == '__main__':
    sumaryPDFs()