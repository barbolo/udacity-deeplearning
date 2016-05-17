# DEPRECATED

############################################################
# Dockerfile to build a deep learning ready image
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Barbolo / Barbolo

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip \
                       python-matplotlib

# Install python libraries
RUN pip install numpy scipy matplotlib
