#!/bin/bash

docker system prune -a -f --volumes --filter "label=maintainer=Ivan Ermilov <ivan.s.ermilov@gmail.com>"