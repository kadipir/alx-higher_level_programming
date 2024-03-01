#!/bin/bash
#sends request to url and invokes the content size to be displayed
curl -s "${1}" | wc -c
