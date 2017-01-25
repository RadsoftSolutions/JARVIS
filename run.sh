#!/usr/bin/env bash

echo "Activating Virtual Environment"
. /Applications/XAMPP/htdocs/work/svn/JARVIS/venv/bin/activate

echo "Initializing JARVIS"
python /Applications/XAMPP/htdocs/work/svn/JARVIS/listen.py