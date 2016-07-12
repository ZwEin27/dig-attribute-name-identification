# dig-attribute-name-identification
identify attribute name and generate dictionary for karma output




## About

DIGANI aims to extract phone numbers from url and text for [DIG](http://usc-isi-i2.github.io/dig/) project. 



## Install

    python setup.py install


## Command Line Usage

enter the WORK_PATH, and run script below

    run-digani $(pwd)

also, you can

    run-digani /<YOU_DIR>/dig-data/sample-datasets/escorts

## Python Usage

    import digani

    digani.run(<WORK_PATH>)

    <WORK_PATH> is the dir contain domains' dataset, such as "/<YOU_DIR>/dig-data/sample-datasets/escorts"

