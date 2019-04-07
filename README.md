# jrj

```
git clone https://github.com/Juaran/jrj.git

cd jrj/jrj_scrapy

sh jrj.sh

如果出现未找到./venv/bin/scrapy等错误
rm -rf venv
重新运行jrj.sh
```

# 1. 配置mysql在piplines.py中设置：
```
HOST      = "192.168.10.145"
PORT      = 3306
USER      = "gophish"
PASSWORD  = "jrjwu"

DATABASE  = "gophish"
TABLE     = "mobile_all"
COLUMN    = "phone"
SAVE_TABLE = "jrj_registered"

STARTPAGE = 0  # 开始页面
ENDPAGE   = 100  # 结束页面
PAGESIZE  = 10000  # 页面大小
```

# 2. 线程设置，在settings.py中设置：
```
修改这一行后面的数值，5即为线程数量
CONCURRENT_REQUESTS = 5
```

# 3. 启动
```
进入项目内
cd jrj_scrapy

执行脚本
sh jrj.sh
```

# 4. 间断后重新运行
根据上一次运行结束时候读取的当前页面，在piplines.py中设置：
```
STARTPAGE = 上次结束页面
```
