FROM python:3.7

# 安装mitmproxy  以及mongo pyyaml
RUN pip install mitmproxy \
    && pip install pymongo \
    && pip install pyyaml

# 创建目录，该目录为挂载文件的目录,存放脚本文件
WORKDIR /script_file

# CMD ["mitmdump", "-p", "8888", "-s", "parse_douyin_fans.py"]



# docker build -t mitmproxy .

# 这里面并不需要暴露端口
# 要在使用的时候：
# 进入到容器内mitmdump -p 8888 -s parse_douyin_fans.py

# 容器启动  ，要在挂载目录下， 启动
# docker run -it -v $PWD:/script_file --name=mitmdump mitmproxy /bin/bash
# /bin/sh -c "while true;do echo hello docker;sleep 1;done"
