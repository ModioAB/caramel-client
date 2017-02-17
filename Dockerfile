FROM registry.gitlab.com/modioab/base-image:fedora-24-python-latest
LABEL maintainer "spider@modio.se"

RUN ["pip3", "install", "caramel-client"]

VOLUME ["/data"]
WORKDIR /data
ENTRYPOINT ["/usr/bin/caramel-client"]
CMD []
