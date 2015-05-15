#!/bin/bash  

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Activate"
    source ./venv/bin/activate;
fi

ipython notebook;
