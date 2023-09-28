# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet

def domain_name(url):
    # 이렇게 쓰면 한줄로도 처리 가능 
    # return url.split("//")[-1].split("www.")[-1].split(".")[0]
    txt = ''
    if len(url.split('//')) == 1:
        txt = url
    else:
        txt = url.split('//')[1]

    list = txt.split('.')

    for word in list:
        if word.startswith('www'):
            list.remove(word)
    
    return list[0]


a = domain_name('www.cnet.com')

if a == 'cnet':
    print('정답!')
else :
    print('오답!')

b = domain_name('http://github.com/carbonfive/raygun')

if b =='github':
    print('정답!')
else :
    print('오답!')   