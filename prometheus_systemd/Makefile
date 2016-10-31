VERSION=1.2.1
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/prometheus/releases/download/v$(VERSION)/prometheus-$(VERSION).linux-amd64.tar.gz -O prometheus-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus-$(VERSION).linux-amd64.tar.gz prometheus-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus.spec

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64.tar.gz"
