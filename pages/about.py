import json, string

def glue(*args):
        retstr = ""
        for arg in args:
                retstr += arg
        return retstr

headerfile = open('/home/koan/koansource/templates/header.html', 'r')
footerfile = open('/home/koan/koansource/templates/footer.html', 'r')
header = headerfile.read()
footer = footerfile.read()

about = header
about = string.replace(about, '{{TITLE}}', 'About')
about = string.replace(about, '{{PAGECSS}}', 'about.css')

about += glue (
'<div class="main">',
	'<div id="leftbox">',
		'<h1>We are KOOAAANNN</h1>',
		'<p>We do</p>',
		'<ul>',
			'<li>This</li>',
			'<li>And this</li>',
			'<li>And this</li>',
			'<li>And this</li>',
			'<li>And even this!</li>',
		'</ul>',
		'<br>',
		'<h2>Things we are proud of</h2>',
		'<p>Bla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla blaBla bla</p>',
		'<br>',
		'<h2>Future plans</h2>',
		'<p>sdbfgkajhbrf, s bksd, f,sdkfhgksdhfbg,kdjf,sjdfgkjsdfgldjgsldkjghskdjfghslkdjfgbsldfgbskdjfgbskdg,jbd,gjdbr,gkkad,jgbsd, </p>',
		'<br>',
		'<h2>Our core beliefs</h2>',
		'<p>Ass and titties, ass ass, titties titties.</p>',
	'</div>',
	'<div id="rightbox">',
		'<h1>Here be a  pretty picture</h1>',
	'</div>',
'</div>')

about += footer

filetoserve = open("/home/koan/koansite/about.html", "w")

filetoserve.write(about)
