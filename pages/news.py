import json, string

def glue(*args):
        retstr = ""
        for arg in args:
                retstr += arg
        return retstr

headerfile = open('/home/koan/koansource/templates/header.html', 'r')
footerfile = open('/home/koan/koansource/templates/footer.html', 'r')
newsitemsfile = open('/home/koan/koansource/database/news.json', 'r')
header = headerfile.read()
footer = footerfile.read()
newsitems = json.loads(newsitemsfile.read())

news = header
news = string.replace(news, '{{TITLE}}', 'News')
news = string.replace(news, '{{PAGECSS}}', 'news.css')

for name, date in newsitems.items():
	news += open('/home/koan/koansource/markdown/' + name, 'r').read()

news += footer

filetoserve = open("/home/koan/koansite/news.html", "w")

filetoserve.write(news)
