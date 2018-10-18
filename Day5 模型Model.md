## MVT目录层级

```python
blog/
	App/
    	__init__.py
        models/ 		模型包文件
        	__init__.py
        views/			蓝本包文件
        	__init__.py
        templates/		模板目录
        	common/
        static/			静态资源目录
        	img/
            css/
            js/
            upload/
         forms/			表单类目录
        	__init__.py
            
        settings.py    配置文件
        extensions.py  第三方扩展库加载
        email.py       发送邮件
           
    migrations/
    venv/
    manage.py
```



## 博客

```python
功能：
登录
	flask-login
注册
重新激活

x个人中心
	查看个人信息
    修改个人信息
    修改用户名
    修改密码
    修改邮箱
    博客管理
    	博客的增删改查
    我的收藏
    
发表博客
首页
	缓存
    	flask-cache
	搜索
    分页
    轮波图
    博客的展示
博客的详情
	博客的展示
    评论和回复
    收藏
    
模型：
	flask-migrate
```



## 分页类

paginatexians

```python
paginate分页类 返回一个分页对象 pagination
参数：
	page 页码 必传 
    per_page 每页显示数据的条数
    error_out 分页出现错误是否抛出错误 默认True
pagination属性：
	items	当前页面所有的数据
    page	当前页码
    pages	所有页码
    total	总记录数
    per_page	每页显示数据的条数
    prev_num	上一页的页码
    next_num	下一页的页码
    has_prev 	是否有上一页
    hash_next	是否有下一页
方法：
	iter_pages	迭代显示所有页码
```



## 缓存 flask-cache

**安装**

pip3 install flask-cache



**配置缓存**

```python
from flask_cache import Cache
cache = Cache(app,config={'CACHE_TYPE':'simple'})
cache = Cache(app,config={'CACHE_TYPE':'redis'})
```



**缓存的方式**

1. @cache.cached 就是页面缓存
2. @cache.memoize 根据视图函数的传参进行缓存



**手动设置缓存**

设置缓存

cache.set(key,value,exprres)

获取缓存

cache.get(key)



### 清除缓存

1. 设置配置文件 缓存过期时间 

   CACHE_DEFAULT_TIMEOUT

2. 给装饰器添加timeout参数值

   @cache.cached(timeout=60)

   @cache.memoize(timeout=60)

3. 清除所有缓存

   cache.clear()

今晚完成的模块：
个人中心除了我的收藏
博客管理完善搜索和分页
详情页面的评论和回复 完成！《样式要完成》















