VERSION=0.4.2
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/alertmanager/releases/download/v$(VERSION)/alertmanager-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz alertmanager-$(VERSION).linux-amd64.tar.gz alertmanager-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/alertmanager.spec

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64.tar.gz"
