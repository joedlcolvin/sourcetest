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
		"<div id='artistflex'>")
for x in range(1,10):
	for name, data in artistsdata.items():
		artists += glue(
			"<div class='artists' id='" + name + "' style='background-color:" + data["Tile Colour"] + "'>",
				"<h2 class='artistname'>" + name + "</h2>",
				"<img class='artistpic' src='/static/images/artists/" + data["Photo"] + "' alt='" + data["Photo"] + " height ='42' width='42'>",
				"<p class='shortbio'>" + data["Short Bio"] + "</p>",
			"</div>")

artists += "</div></div>"

artists += footer

filetoserve = open("/home/koan/koansite/artists.html", "w")

filetoserve.write(artists)
