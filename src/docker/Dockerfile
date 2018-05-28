
FROM ubuntu:16.04

MAINTAINER jeffeb3

# sudo doesn't work in docker containers, replace it with gosu, by way of a sudo.sh
COPY sudo.sh /usr/bin/sudo
COPY sudo.sh /usr/local/bin/sudo

# Found from: https://github.com/tianon/gosu/blob/master/INSTALL.md
ENV GOSU_VERSION 1.10
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +xs /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget


RUN set -x \
    && apt-get update && apt-get install -y \
        build-essential \
        curl \
        git \
        wget \
        realpath \
        p7zip-full \
        python3 \
        binfmt-support \
        qemu \
        qemu-user-static \
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
