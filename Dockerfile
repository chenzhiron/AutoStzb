   FROM python:3.9

   WORKDIR /app

   # 将项目所需的依赖项复制到容器中
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   # 将整个项目复制到容器中

   # 设置容器的入口命令
   CMD ["python", "app.py"]
