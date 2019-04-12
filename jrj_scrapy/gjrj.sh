#!/bin/bash

venv/bin/pip3 list | grep PyMySQL > /dev/null
if [ $? -eq 0 ]
then
    echo "PyMySQL Installed. "
else
    echo "Installing PyMySQL..."
    venv/bin/pip3 install pymysql > /dev/null
    echo "[ OK ]"
fi


# 运行
venv/bin/scrapy crawl jrj --nolog
