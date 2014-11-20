import os,urllib,urllib2

def postContent(access_token,blogid,asin):
    tagID = 'jewelrythatma-20'
    asin = asin.strip()
    linkOffer = 'http://www.amazon.com/gp/offer-listing/{0}/ref=as_li_tf_tl?ie=UTF8&creativeAS={0}\
&link_code=am3&tag={1}'.format(asin,tagID)
#    print linkOffer
    linkDetail = 'http://www.amazon.com/gp/product/{0}/ref=as_li_tf_tl?ie=UTF8&creativeASIN={0}\
&link_code=as3&tag={1}'.format(asin,tagID)
#    print linkDetail
    attempts = 0
    ###################
    ####  begin
    ###################
    reqUrl = 'http://astore.amazon.com/bladmusik/detail/'+asin
    user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    values = {'name': "pui",
              'location': 'Thai'}
    headers = { 'User-Agent': user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(reqUrl,data,headers)
    res = urllib2.urlopen(req)
    doc = res.read()
    w  = open('o2.txt','w')
    w.write(doc)
    w.close()
    print reqUrl
    
    
