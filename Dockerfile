FROM registry.gitlab.com/modioab/base-image:fedora-24-python-latest
LABEL maintainer "spider@modio.se"

ENV LANG  C.utf8
ENV LANGUAGE en_US:en
ENV LC_ALL C.utf8

RUN ["pip3", "install", "caramel-client"]

VOLUME ["/data"]
WORKDIR /data
ENTRYPOINT ["/usr/bin/caramel-client"]
CMD []
