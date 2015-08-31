#coding=utf-8
import lxml.html as HTML
import urllib
def parse(html_content, xpath, charset='utf8'):
    html = html_content.decode(charset, 'ignore')
    #html = html_content
    tree = HTML.fromstring(html)
    boards = tree.xpath(xpath)
    return boards

def html_parse(url, xpath, charset="utf8"):
    html = urllib.urlopen(url).read()
    boards = parse(html, xpath, charset) # call for fun
    #print len(html), xpath, boards
    art = []
    for node in boards:
        #tag = node.tag.encode('gbk')
        content = node.text_content().encode('gbk', 'ignore').strip('\r\n ')
        #ll = len( node.text_content().encode('gbk', 'ignore'))
        #print "%d,%s,%s,%s" % (idx,tag,content,ll)
        #print content
        art.append(content) # res_data_ul_content
    return art


if __name__=='__main__':
    art = html_parse('http://www.beijing.gov.cn/tzbj/hzfw/t1400931.htm', '//h1/div/p/span | /html/body/div/div/div/ul/li | /html/body/div/div/div//div/p', "gbk")
    print "***%s\n***%s\n***%s\n" %(art[0],art[1],art[2])
    print "***т╜нд:" , (art[3:])
