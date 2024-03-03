#!/bin/bash
# post contents of a file
curl -s "${1}" -d "@$2" -X POST  -H "Content-Type: Application/JSON"
