FROM frolvlad/alpine-python3:latest

MAINTAINER Kevin Smith <kevin@operable.io>

# Install newer certs and pycog3
RUN apk update && \
  apk add ca-certificates wget && \
  ln -s /usr/bin/python3 /usr/bin/python && \
  rm -rfv /var/cache/apk/*

RUN adduser -h /home/bundle -D bundle

USER root
WORKDIR /home/bundle
RUN wget -q https://github.com/cog-bundles/pycog3/archive/0.1.26.tar.gz && \
    tar xzvf 0.1.26.tar.gz && \
    cd pycog3-0.1.26 && pip3 install . && pip3 install -r requirements.txt && \
    cd .. && rm -rf pycog3* && mkdir -p /home/bundle/statuspage/statuspage/commands

COPY setup.py requirements.txt /home/bundle/statuspage/
COPY statuspage/*.py /home/bundle/statuspage/statuspage/
COPY statuspage/commands/*.py /home/bundle/statuspage/statuspage/commands/

WORKDIR /home/bundle/statuspage
RUN pip3 install .