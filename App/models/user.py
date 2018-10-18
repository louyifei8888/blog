from App.extensions import db
from datetime import datetime
from .commonbaseclass import Base #增删改的基类
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from flask import current_app
from flask_login import UserMixin
from .posts import Posts

#用户模型类
class User(UserMixin,Base,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(12),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Boolean,default=True)
    age = db.Column(db.Integer,default=18)
    email = db.Column(db.String(50),unique=True) #邮箱
    icon = db.Column(db.String(70),default='default.jpg') #头像
    lastLogin = db.Column(db.DateTime) #上次登录时间
    registerTime = db.Column(db.DateTime,default=datetime.utcnow) #注册时间
    confirm = db.Column(db.Boolean,default=False) #激活状态 默认不激活
    """
    添加反向引用的关系
    参数1 和哪一个模型建立关联
    参数2 给参数1的模型添加一个模型属性 user
    参数3 加载时机 dynamic返回查询的对象 可以链式调用 如果不填加/select 则u.posts直接返回数据的结果 不能进行model的过滤器的链式调用
    u.posts.all() 获取所有u对象发表的博客
    p.user  获取当前发表博客的用户对象
    """
    posts = db.relationship('Posts',backref='user',lazy='dynamic')
    # secondary 指定多对多关系 查询的指定中间表
    #zhangsan.favorites.append(博客对象)
    #zhangsan.favorites.remove(博客对象)
    #zhangsan.favorites.all() #用户收藏了哪些博客
    #p.user.all() #都被谁收藏了
    favorites = db.relationship('Posts',secondary='collections',backref=db.backref('users',lazy='dynamic'),lazy='dynamic')
    #密码加密处理
    @property
    def password(self):
        raise AttributeError

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    #检测密码正确性
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    #token值的生成
    def generate_token(self):
        s = Seralize(current_app.config['SECRET_KEY']) #生成token对象
        return s.dumps({'id':self.id}) #通过给定字典生成token字符串

    #账户的激活
    @staticmethod
    def check_token(token):
        try:
            s = Seralize(current_app.config['SECRET_KEY'])  # 生成token对象
            id = int(s.loads(token)['id']) #通过token值加载出字典
            u = User.query.get(id) #拿到访问者的对象
            u.confirm = True #修改激活状态
            u.save() #保存
            return True
        except:
            return False

    #定义一个判断是否收藏的方法
    def is_favorite(self,pid):
        favorites = self.favorites.all()
        for i in favorites:
            if i.id==pid:
                return True
        return False
    #收藏
    def add_favorite(self,pid):
        self.favorites.append(Posts.query.get(pid))
        db.session.commit()


    #取消收藏
    def remove_favorite(self,pid):
        self.favorites.remove(Posts.query.get(pid))
        db.session.commit()


    def __str__(self):
        return self.username


#回调函数 时刻从数据库中获取 当前用户的最新数据
from App.extensions import login_manager
@login_manager.user_loader
def user_loader(userid):
    return User.query.get(int(userid))