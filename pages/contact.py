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

contact = header
contact = string.replace(contact, '{{TITLE}}', 'Contact')
contact = string.replace(contact, '{{PAGECSS}}', 'contact.css')

contact += glue (
'<div class="main">',
	'<h1>Want to get in touch?</h1>',
		'<ul>',
			'<li>Facebook:</li>',
			'<li>Twitter:</li>',
			'<li>Instagram:</li>',
			'<li>Email:</li>',
			'<li>Carrier pigeon</li>',
		'</ul>',
'</div>')

contact += footer

filetoserve = open("/home/koan/koansite/contact.html", "w")

filetoserve.write(contact)
