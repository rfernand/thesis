NAME=thesis
NAME_SHORT=short
BIN=bin

FLAGS=-output-directory $(BIN)

all:	pdf clean
short:  shortpdf shortclean

shortpdf:
	@rubber -d $(NAME_SHORT)
	@mkdir -p bin
	@mv $(NAME_SHORT).pdf bin/

shortclean:
	@rubber --clean $(NAME_SHORT)

pdf:
	@rubber -d $(NAME)
	@mkdir -p bin
	@mv $(NAME).pdf bin/

clean:
	@rubber --clean $(NAME)


.PHONY: all clean distclean k
