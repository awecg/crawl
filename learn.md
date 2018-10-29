网页下载器  ulrlib2  requests
网页解析器  正则表达式    html.paser  Beautiful Soup   lxml
+ 结构化解析 遍历DOM



### python
```python
print os.getcwd()
print sys.path[0]
```

> if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。

+ python3中urlparse模块和urllib模块合并，urlparse()在urllib.parse中进行调用。
+ 解决url中文编码 urllib.unquote()