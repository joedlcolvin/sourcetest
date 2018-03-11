import json, string

def glue(*args):
        retstr = ""
        for arg in args:
                retstr += arg
        return retstr

headerfile = open('/home/koan/koansource/templates/header.html', 'r')
footerfile = open('/home/koan/koansource/templates/footer.html', 'r')
artistsdatafile = open('/home/koan/koansource/database/artists.json', 'r')
header = headerfile.read()
footer = footerfile.read()
artistsdata = json.loads(artistsdatafile.read())

artists = header
artists = string.replace(artists, '{{TITLE}}', 'Artists')
artists = string.replace(artists, '{{PAGECSS}}', 'artists.css')

artists += glue(
	"<div id='main'>",
		"<div id='artist-display-container'>")
for name, data in artistsdata.items():
	artists += glue(
			"<div class='artist-display' id='ad" + data["Order Number"] + "'>",
					"<h1 class='artistname'>" + name + "</h1>",
					"<img class='artistpic' src='/static/images/artists/" + data["Photo"] + "' alt='" + data["Photo"] + " height ='42' width='42'>",
				"<p class='longbio'>" + data["Full Bio"] + "</p>",
			"</div>")

artists += glue("</div>",
		"<div id='list-container'>",
			"<div id='leftbutton'>",
			"</div>",
			"<div id='rightbutton'>",
			"</div>",
			"<div id='artist-list>")
for name, data in artistsdata.items():
	artists += glue(
				"<div id='a" + data["Order Number"] + "' class='artist'>",
					"<h2>" + name + "</h2>",
					"<p>" + data["Short Bio"] + "</p>",
				"</div>")

artists += glue(	"</div>",
		"</div>",
	"</div>")

artists += footer

filetoserve = open("/home/koan/koansite/artists.html", "w")

filetoserve.write(artists)
