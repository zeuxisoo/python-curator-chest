### Curator Chest

A simple script for you save all girls from the stream in [cuator.im](http://curator.im/)

### Install

Clone the repository

	git clone https://github.com/zeuxisoo/python-curator-chest.git

Create the environment

	cd python-curator-chest
	virtualenv-2.7 --no-site-package venv
	source venv/bin/activate
	pip install -r requirements.txt

### Usage

Save all photo from stream

    python drop.py -t [TOKEN]

Save all photo from stream with 5 worker

	python drop.py -t [TOKEN] -w 5
	
Save to specified directory

	python drop.py -t [TOKEN] -o /home/user/Desktop/mybox
	
Save log file

    python drop.py -t [TOKEN] >> ./log.txt
    
Print usage

	python drop.py