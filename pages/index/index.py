import json

headerfile = open('/home/koan/koansource/templates/header.html', 'r')
footerfile = open('/home/koan/koansource/templates/footer.html', 'r')
carouselfile = open('/home/koan/koansource/database/carousel.json', 'r')
header = headerfile.read()
footer = footerfile.read()
carousel = json.loads(carouselfile.read())
print carousel

index = header
index.replace('{{TITLE}}', 'Index')
index.replace('{{PAGECSS}}', 'index.css')

index += ""
"<div class='main'>"
"<div class='slideshow-container'>"
i = 0
for image, caption in carousel:
	i = i + 1	
	index += ""
"<div class='mySlides fade'>"
"<div class='numbertext'>" + str(i) + " / " + str(len(carousel)) + "</div>"
"<img class='image' src='/home/koan/koansite/static/images/carousel/" + image + "' %} style='width:100%; '>"
"<div class='text'><p>" + caption + "</p></div>"
"</div>"

index += ""
"<a class='prev' onclick='plusSlides(-1)'>&#10094;</a>"
"<a class='next' onclick='plusSlides(1)'>&#10095;</a>"
"</div>"
"<br>"
""
"<!-- The dots/circles -->"
"<div style='text-align:center'>"

for x in range(0,len(carousel)):
	index += " <span class='dot' onclick='currentSlide(" + str(x+1) + ")'></span>"

index += "</div>"

index += "<div id='flexcontent'>"
"<div id='leftbox'>"
"<div id='news'>"
"<h1>News</h1>"
"<ul>"
"<li>News item #1: bla</li>"
"<li>News item #2: bla</li>"
"<li>News item #3: bla</li>"
"<li>News item #4: bla</li>"
"<li>News item #5: bla</li>"
"</ul>"
"</div>"
"<iframe id='youtube' width='560' height='315' src='https://www.youtube.com/embed/P74F-R_TBu8' frameborder='0' gesture='media' allow='encrypted-media' allowfullscreen></iframe>"
"</div>"
"<div id='rightbox'>"
"<h1>SPOTIFY</h1>"
"<h1>BANDCAMP</h1>"
"</div>"
"</div>"
"</div>"

index += footer
