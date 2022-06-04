
html: resume.html

all: html

resume.html: resume.rst resume.css rst2html.py 
	./rst2html.py \
		--traceback \
		--stylesheet-path=minimal.css,plain.css,./resume.css \
		resume.rst > $@
		

clean: 
	rm resume.html

.PHONY: all html clean
