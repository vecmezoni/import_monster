PACKAGES="import_monster"

all: install black

black:
	@black ${PACKAGES}

install:
	@pip install -r requirements.txt
