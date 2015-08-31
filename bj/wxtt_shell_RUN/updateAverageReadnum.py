#coding:gbk
import sys

#get openid readnums
openid_readnum = {}
if __name__ == '__main__':
        cnt = 0
        for line in sys.stdin:
                if cnt % 1000000 == 0:
                        sys.stderr.write('%d lines \n' % cnt)
                cnt += 1
                vec = line.strip().split('\t')
                if len(vec) < 7:
                        continue
                openid = vec[4]
                try:
                    readnum = int(vec[3])
                except:
                    continue
                if openid not in openid_readnum:
                        openid_readnum[openid] = []
                openid_readnum[openid].append(readnum)
        #fw = open('log/update_openid_averagereadnum.log','w')
        #openid_readnum = {'oIWsFt97NeXcgGqdAows9NzOjmv8':[88]}
        for openid in openid_readnum:
                averagereadnum = sum(openid_readnum[openid]) * 1.0 / len(openid_readnum[openid])
                print openid + '\t' + str(averagereadnum)
