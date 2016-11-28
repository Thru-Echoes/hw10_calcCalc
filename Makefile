NS = Thru-Echoes
VERSION = latest
NAME = mydocker
REPO = hw10_calcCalc
PORTS = -p 5000:5000
INSTANCE = default
VOLUMES = -v /tmp/docker:/var/log

build:
	docker build -t $(NS)/$(REPO):$(VERSION) .

run:
	#docker rm $(NAME)-$(INSTANCE)
	docker run -d --name $(NAME)-$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

shell: run
	docker exec -it $(NAME)-$(INSTANCE) /bin/sh

default: build
