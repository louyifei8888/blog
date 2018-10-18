from flask import Flask
from .extensions import ext_init
from .settings import configDict
from .views import register_blueprint
from App.models import Posts
#整个项目的加载
def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName]) #配置文件的加载
    ext_init(app)
    register_blueprint(app)
    add_tem_filter(app) #自定义模板过滤器
    return app



def add_tem_filter(app):
    #超出 内容长度显示...
    def show_point(con,myLength=80):
        length = len(con)
        if length>myLength:
            con = con[0:myLength]+'...'
        return con

    #将搜索的内容替换成红色的字
    def replace_color(con,word):
        con = con.replace(word,'<span style="color:red;font-size:20px;">'+str(word)+'</span>')
        return con

    #回复用户名的显示
    def replay_username(pid):
        return Posts.query.get(int(pid)).user.username

    app.add_template_filter(replay_username)
    app.add_template_filter(show_point)
    app.add_template_filter(replace_color)



