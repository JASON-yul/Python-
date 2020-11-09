# -*- coding:UTF-8 -*-
# -*- create on 2019/06/28 by HangLi -*-
import os
import sys

def get_fname(fname):
#  while True:
#    if not os.path.exists(fname):
#      break
#    print('file is true')
  return fname

def get_content(content):
    content.append(sys.argv[0])
    return content
def wfile(f,c):
  with open(f,'w') as fobj:
    fobj.writelines(c)

if __name__ == '__main__':
    fname = sys.argv[1]
    content = []
    f = get_fname(fname)
    c = get_content(content)
    wfile(f,c)
