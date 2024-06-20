#!/bin/bash
set -eux
docker push tamuto/proxiquery:$1
docker push tamuto/proxiquery:latest
