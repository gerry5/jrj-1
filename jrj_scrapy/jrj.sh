#!/bin/bash

# 检查python3
which python3 > /dev/null
if [ $? -eq 0 ]
then
    echo "Python3 Exists. [ OK ]"
fi

# 检查pip3
which pip > /dev/null
if [ $? -eq 0 ]
then
    echo "Pip3 Exists. [ OK ]"
else
    echo "Install Pip3..."
    sudo apt-get install python3-pip
    echo "[ OK ]"
    echo "Upgrade Pip3..."
    pip3 install --upgrade pip
    echo "[ OK ]"
fi

# 检查虚拟环境
ls | grep venv > /dev/null
if [ $? -eq 0 ]
then
    echo "Venv Exists. [ OK ]"
else
    echo "Venv Not Found. Creating..."
    python3 -m venv venv

    # 为空则成功，否则安装
    if [ $? -eq 0 ]
    then
        echo "Python3-venv Not Exists. Installing..."
        sudo apt-get install python3-venv
        echo "[ OK ]"
    else
        echo "[ OK ]"
    fi

    echo "[ OK ]"
fi

# 检查Scrapy包
venv/bin/pip3 list --format=columns | grep Scrapy > /dev/null
if [ $? -eq 0 ]
then
    echo "Scrapy Installed. "
else
    echo "Installing Scrapy..."
    venv/bin/pip3 install scrapy > /dev/null
    echo "[ OK ]"
fi

# 检查Pymysql包
venv/bin/pip3 list --format=columns | grep PyMySQL > /dev/null
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