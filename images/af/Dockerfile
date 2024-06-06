# syntax=docker/dockerfile:1

FROM ubuntu:jammy

# build-time arguments
ARG DEBIAN_FRONTEND="noninteractive"

# install dependencies
RUN apt-get update && apt-get install iproute2 sendip iputils-ping dnsutils curl -y

# copy entrypoint scripts
COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
