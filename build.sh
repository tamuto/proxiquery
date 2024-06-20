#!/bin/bash
set -eux
docker build -t tamuto/proxiquery:$1 .
docker tag tamuto/proxiquery:$1 tamuto/proxiquery:latest
