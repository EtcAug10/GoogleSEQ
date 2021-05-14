import requests,sys,re
from urllib.parse import unquote

if len(sys.argv) == 3:
  kueri = sys.argv[1]
  page = int(sys.argv[2])

  for a in range(page):
    try:
      r = requests.get("https://google.com/search?q=%s&start=%s&num=%s" % (kueri,int(a)*10,10))
      p = re.findall(r"href=\"\/url\?q\=(.*?)\&amp",r.text)
      for a in p:
        if re.search("accounts.google",a) or re.search("support.google",a): 
          pass
        else:
           print(unquote(a))
    except:
      break
else:
  print("""
Google SE Query -
   -   Made By AryaKun

USAGE:
	python gse.py [KUERI] [JUMLAH HALAMAN]
EXAMPLE:
	python gse.py "inurl:.php?id=20 site:.il" 10
	python gse.py cecans 7

\\\\--\\-\\-\\-\\-\\-\\-\\-\\\\
©jawarahacking.com

""")
