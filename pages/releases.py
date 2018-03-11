import json, string

def glue(*args):
        retstr = ""
        for arg in args:
                retstr += arg + "\n"
        return retstr

header = open('/home/koan/koansource/templates/header.html', 'r').read()
footer = open('/home/koan/koansource/templates/footer.html', 'r').read()
releaseitems = json.loads(open('/home/koan/koansource/database/releases.json', 'r').read())

releases = header
releases = string.replace(releases, '{{TITLE}}', 'Releases')
releases = string.replace(releases, '{{PAGECSS}}', 'releases.css')
releases = string.replace(releases, '{{PAGEJS}}', 'releases.js')

releases += glue(
	'<div class="main">',
		'<div id="flexcontent">',
			'<div id="leftbox">',
				
			'</div>',
			'<div id="rightbox">',
			'</div>',
		'</div>',
	'</div>')

releases += footer

filetoserve = open("/home/koan/koansite/releases.html", "w")

filetoserve.write(releases)

