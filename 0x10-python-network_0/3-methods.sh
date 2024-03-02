#!/bin/bash
#list method requests allowed
curl -s -I "4{1}" | grep "^allow: .*" | cut -d " " -f 2-
