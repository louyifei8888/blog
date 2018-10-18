from .user import User
from .posts import Posts
from App.extensions import db

# 创建多对多中间表 存储多对多的id
collections = db.Table('collections',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('posts_id',db.Integer,db.ForeignKey('posts.id')),
)