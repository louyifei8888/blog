from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import DataRequired,Length

#博客表单
class Posts(FlaskForm):
    title = StringField('标题',validators=[DataRequired('标题不能为空'),Length(min=3,max=20,message='标题内容长度在3～20字之间')],render_kw={'placeholder':'输入标题...','minlength':3,'maxlength':20})
    content = TextAreaField('博客内容',validators=[DataRequired('内容不能为空'),Length(min=20,max=4000,message='博客内容在20～4000字之间')],render_kw={'placeholder':'请输入博客内容','minlength':20,'maxlength':4000})
    submit = SubmitField('发表')