from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from App.models import User #导入User模型类

#注册表单类
class Register(FlaskForm):
    username = StringField('用户名',validators=[DataRequired('用户名不能为空'),Length(min=6,max=12,message='用户名6～12位之间')],render_kw={'placeholder':'请输入用户名','minlength':6,'maxlength':12})
    userpass = PasswordField('密码',validators=[DataRequired('密码不能为空'),Length(min=6,max=12,message='密码6～12位之间')],render_kw={'placeholder':'请输入密码','minlength':6,'maxlength':12})
    confirm = PasswordField('确认密码',validators=[DataRequired('确认密码不能为空'),Length(min=6,max=12,message='确认密码～12位之间'),EqualTo('userpass',message='密码和确认密码不一致')],render_kw={'placeholder':'请输入确认密码','minlength':6,'maxlength':12})
    email = StringField('激活邮箱',validators=[DataRequired('邮箱不能为空'),Email('请输入正确的邮箱地址')],render_kw={'placeholder':'请输入用于激活账户注册的有效的邮箱地址'})
    submit = SubmitField('注册')
    #验证用户名唯一性
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在 请重新输入')

    # 验证邮箱唯一性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已存在 请重新输入')

#再次激活表单类
class AgainActivate(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空'), Length(min=6, max=12, message='用户名6～12位之间')],
                           render_kw={'placeholder': '请输入用户名', 'minlength': 6, 'maxlength': 12})
    userpass = PasswordField('密码', validators=[DataRequired('密码不能为空'), Length(min=6, max=12, message='密码6～12位之间')],
                             render_kw={'placeholder': '请输入密码', 'minlength': 6, 'maxlength': 12})
    submit = SubmitField('激活')

    # 验证用户名是否存在
    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名不存在 请重新输入')



#登录表单类
class Login(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空'), Length(min=6, max=12, message='用户名6～12位之间')],
                           render_kw={'placeholder': '请输入用户名', 'minlength': 6, 'maxlength': 12})
    userpass = PasswordField('密码', validators=[DataRequired('密码不能为空'), Length(min=6, max=12, message='密码6～12位之间')],
                             render_kw={'placeholder': '请输入密码', 'minlength': 6, 'maxlength': 12})
    remember = BooleanField('记住我')
    submit = SubmitField('登录')

    # 验证用户名是否存在
    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名不存在 请重新输入')
