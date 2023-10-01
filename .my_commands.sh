#!/bin/bash

function create() {
    cd /home/dtisoy/projects/ProjectInitializationAutomation

    source .env
    source venv/bin/activate
    python3 create.py $1
    deactivate
    cd $FILEPATH$1
    git init
    git remote add origin git@github.com:$USERNAME/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master

}
