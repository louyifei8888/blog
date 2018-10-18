import os

#配置文件
class Config:
    SECRET_KEY = 'ssd912hjkdsa01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.1000phone.com'   # 邮箱服务器
    MAIL_USERNAME = 'xialigang@1000phone.com'  # 填邮箱
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')      # 填授权码
    #每页显示数据的条数
    PAGE_NUM = 5

# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python1805dev_blog'
    DEBUG = True
    TESTING= False

#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python1805test_blog'
    DEBUG = False
    TESTING= True

#生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    DEBUG = False
    TESTING= False

#配置的字典
configDict = {
    'default':DevelopmentConfig,
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'Product':ProductionConfig
}




