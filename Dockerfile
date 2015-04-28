FROM ubuntu:14.04
MAINTAINER Robert George <robert@poovelil.org>
RUN apt-get update && apt-get install -y python-dev \
	    curl \
	    libffi-dev \
	    libssl-dev \
	    libxml2-dev \
	    libxslt1-dev
RUN  curl -L https://bootstrap.pypa.io/get-pip.py | python
RUN pip install Scrapy
RUN pip install service_identity

