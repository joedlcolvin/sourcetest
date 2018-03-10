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

releases += glue(
	'<div class="main">',
		'<div id="flexcontent">',
			'<div id="leftbox">')

for release in releaseitems:
	if release['type'] == "video":
		releases += glue(
				'<div class="video-release-box">',
					'<iframe class="video" title="' + release['title'] + '" data-releasedate="' + release['releasedate'] + '" data-artists="') 

		for artist in release['artists']:
			releases += artist + ","

		releases += glue(
				'" width="560" height="315" src="' + release['link'] + '" frameborder="0" style="flex-grow:' + release['tile size'] + '" gesture="media" allow="encrypted-media" allowfullscreen></iframe>',
				'</div>',)
				
releases += glue(
			'</div>',
			'<div id="rightbox">')


for release in releaseitems:
	if release['type'] == "track":
		releases += glue(
				'<iframe title="' + release['title'] + '" data-releasedate="' + release['releasedate'] + '" data-artists="') 

		for artist in release['artists']:
			releases += artist + ","

		releases += glue(
				'" width="100%" height="166" src="' + release['link'] + '" frameborder="no" scrolling="no"></iframe>')

releases += glue(
			'</div>',
		'</div>',
	'</div>')

releases += footer

filetoserve = open("/home/koan/koansite/releases.html", "w")

filetoserve.write(releases)

