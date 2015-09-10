#coding=utf-8
import lxml.html as HTML
import urllib
def parse(html_content, xpath, charset='utf8'):
    html = html_content.decode(charset, 'ignore')
    #html = html_content
    tree = HTML.fromstring(html)
    boards = tree.xpath(xpath)
    return boards

def test(url, xpath, charset="utf8"):
    html = urllib.urlopen(url).read()
    boards = parse(html, xpath, charset) # call for fun
    print len(html), xpath, boards
    idx = 0
    l = []
    for node in boards:
        #l.append((idx, node.tag, node.text_content().encode('gbk', 'ignore').strip('\r\n '),  node.get("href"), node.get("class"), len( node.text_content().encode('gbk', 'ignore'))))
        #print  idx, node.tag, node.text_content().encode('gbk', 'ignore').strip('\r\n '),  node.get("href"), node.get("class"), len( node.text_content().encode('gbk', 'ignore'))
        #print "****" , node
        tag = node.tag.encode('gbk')
        title = node.text_content().encode('gbk', 'ignore').strip('\r\n ')
        new_url = node.get("href")
        if new_url[:7] != "http://":
            new_url = format_url( url,new_url)
        cla = node.get("class")
        ll = len( node.text_content().encode('gbk', 'ignore'))
        print "%d,%s,%s,%s,%s,%s" % (idx,tag,title,new_url,cla,ll)
        #print idx, node.tag , node.get("class")
        idx += 1
    return l
# 返回下标
def str_find(url,pat,index):
    for idx in range(len(url)):
        if pat == url[idx]:
            index -= 1
            if(not index): return idx
    return -1
# 反转字符串 为新的串，旧的不便
def r_str_find(url,pat,index):
    ls = list(url)
    ls.reverse()
    r_url = ''.join(ls)
    return str_find(r_url,pat,index)
# 合成新的url
def format_url(url,new_url):
    idx = str_find(new_url,'.',2) # 查找第二个.
    if idx == 1:
        r_idx = r_str_find(url,'/',2)
        #print "pyz",new_url[idx+1:]
        return (url[:-r_idx] + new_url[idx+2:]) # ../
    idx = str_find(new_url,'.',1)
    if idx == 0:
        r_idx = r_str_find(url,'/',1)
        return (url[:-r_idx] + new_url[idx+2:]) # ./
    return new_url


if __name__=='__main__':
    #test('http://www.cankaoxiaoxi.com/', "/html/body//div[@class='hot ov']//a |//div[starts-with(@class, 'main_right')]//ul[@class='yaowen yaospec']//a")
    #test('http://mil.cankaoxiaoxi.com/', '/html/body/div[4]/div[1]//a')
    #test('http://science.cankaoxiaoxi.com/', '//div[@id="conlist"]//a[@title]')
    #test('http://money.163.com/', '//div[@class="fn_focus_news"]//h2//a | //div[starts-with(@class, "fn_three_cat")]//a', "gbk")
    #test('http://ent.163.com/', '//*[@id="ent_index_content"]/div[2]/div[1]//h2//a|//div[@class="list-news"]//h2//a', "gbk")
    #test('http://sports.163.com/', '//div[@class="focus_body"]//a|//div[@class="col_l"]//h2|/html/body/div[2]/div[3]/div[1]/div[1]//li//a ', "gbk")
    #test('http://tech.163.com/', '//h2[@class="color-link"]//a', "gbk")
    #test('http://tech.163.com/', '//h2[@class="color-link"]//a', "gbk")
    #test('http://www.ifeng.com/', '//div[@id="headLineDefault"]//a', "utf8")
    #test('http://news.ifeng.com/mil/', '//div[@id="photolist_66"]//a|//h1//a|//ul[@class="list01"]//a', "utf8")
    #test('http://ent.ifeng.com/', '//p[@class="cWhite"]//a | //div[@class="box_01"]//h2//a | //div[@class="box_02"]//ul//a', "utf8")
    #test('http://tech.ifeng.com/', '//div[@class="mtxt01"]//a | //div[@class="colL"]//h3//a | //div[@class="colL"]//h2//a', "utf8")
    #test('http://finance.ifeng.com/', '//div[@class="w400"]//h2//a|//div[@class="box_02 mb18"]//h3//a|//div[@class="box_02 mb18"]//li//a', "utf8")
    #test('http://sports.ifeng.com/', '//div[@class="col_01_lm"]//a', "utf8")
    #test('http://news.sohu.com/', '//div[@class="r"]//a', "gbk")
    #test('http://news.qq.com/', '//div[@id="headingNews"]//h2//a|//div[@id="mainTabPanel0"]//em//a', "gbk")
    #test('http://finance.qq.com/', '//div[@class="headNews yh"]//h2//a|//div[@class="listbox mt15"]//a', "gbk")
    #test('http://ent.qq.com/', '//ul[@class="focusImgs"]//h3//a|//ul[@class="hotNews"]//h3//a', "gbk")
    #test('http://sports.qq.com/', '//ul[@class="focusImgs"]//h3//a|//div[@bosszone="Headline"]//a', "gbk")
    #test('http://mil.news.sina.com.cn/', '//div[@class="p1"]//a', "gbk")
    #test('http://finance.sina.com.cn/', '//div[@id="impNews1"]//a', "gbk")
    #test('http://tech.qq.com/', '//div[@class="chief"]//a', "gbk")
    #test('http://tech.sina.com.cn/', '//div[@class="blk11 clearfix"]//a', "utf8")
    #test('http://news.sina.com.cn/', '//div[@id="blk_yw_01"]//a', "utf8")

    #test('http://ent.sina.com.cn/', '//div[@class="important-news"]//a', "utf8")
    #test('http://sina.cn/?vt=4&pos=3', '//div[@class="top_news"]//a|//section[@id="card_yaowen"]//a', "utf8")
    #test('http://3g.163.com/touch/', '//div[@id="m-focusImage"]//a|//article[@class="m-newsfocus m-news debug-hide"]//h2//a|//article[@class="m-emphasis m-news debug-hide"]//a', "utf8")
    #test('http://news.163.com/', '//*[@id="ne_wrap"]/body/div[2]/section[3]//a | //*[@id="ne_wrap"]/body/div[2]/section[5]//a | //*[@id="ne_wrap"]/body/div[2]/section[7]//a', "gbk") # the qian yige mulu
    #test('http://ent.cankaoxiaoxi.com/', '//div[@class="ov"]//h2//a', "utf8")
    #test('http://sports.sohu.com/', '//div[@class="center"]//a', "gbk")
    #test('http://mil.sohu.com/', '//div[@class="c-m-r"]//a', "gbk")
    #test('http://yule.sohu.com/', '//*[@id="focus"]/div[2]/div[5]/div[1]//a', "gbk")
    ##test('http://3g.sohu.com/c/2/?_once_=000025_top_xinwen_v3', '//section[@class="hn hn1"]//h4//a', "utf8")
    #test('http://news.qq.com/', '//div[@id="mainTabPanel0"]//a', "gbk")
    #test('http://news.163.com/mobile/', '/html/body/div/section/h3/a', "gbk")
    #test('http://news.163.com/mobile/', '//div/section//a', "gbk")
    #test('http://zhengwu.beijing.gov.cn/gzdt/default.htm', '//body/div[3]/div[2]/div[3]//a', "gbk")
    #test('http://zhengwu.beijing.gov.cn/gzdt/default.htm', '/html/body/div[3]/div[2]/div[3]/ul[1]//a | //ul/li/a', "gbk")
    test('http://www.beijing.gov.cn/sy/rdgz/', '//body/div/ul//a', "gbk")
