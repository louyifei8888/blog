from datetime import datetime
from App.extensions import db
from .commonbaseclass import Base #增删改的基类

class Posts(Base,db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20)) #标题
    content = db.Column(db.Text) #博客内容
    pid = db.Column(db.Integer,default=0) #pid为0则为博客 否则为评论和回复
    path = db.Column(db.Text,default='0,') #路径path
    visit = db.Column(db.Integer,default=0) #访问量
    timestamp = db.Column(db.DateTime,default=datetime.utcnow) #发表的时间
    state = db.Column(db.Boolean,default=True) #默认所有人可见
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))
    def __str__(self):
        return self.title




