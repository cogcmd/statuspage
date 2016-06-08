FROM frolvlad/alpine-python3:latest

MAINTAINER Kevin Smith <kevin@operable.io>

# Install newer certs and git
RUN apk update && \
  apk add ca-certificates && \
  pip3 install pygerduty-py3 && \
  rm -rfv /var/cache/apk/*