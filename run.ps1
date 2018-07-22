#!/bin/bash

docker run --name test_app_container -it -d -p 8080:8080 app:latest