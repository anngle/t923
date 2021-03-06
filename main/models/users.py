#coding=utf-8
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
# from flask_login import UserMixin
from flask_rbac import UserMixin

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
from main.extensions import bcrypt,rbac

import datetime

from main.models.recommend import Recommend
from main.models.buys_car import BuysCar



users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)



@rbac.as_user_model
class User( SurrogatePK, Model,UserMixin):
    """用户表.

    表名称：users

    列名称：
     - username：用户名
     - password：密码 ，hashed password
     - created_at：创建时间
     - name：姓名
     - active：是否激活。默认false
     - active_at：激活时间，默认当前时间
     - is_admin：是否管理员
     - is_center：是否报单中心
     - phone：手机号，用于登录等
     - buys_id：外键引用 产品购买表
     - integral:积分
     - coins:硬币
     - parent_center：引用自身 上级
     - children_center：引用自身
     - recommends：引用推荐表
     - recommender：外键引用推荐人表
     - buys_car_id:外键购物车

    """
    __tablename__ = 'users'

    username = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(128), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    name = Column(db.String(30))
    active = Column(db.Boolean(), default=False)
    active_at = Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    is_admin = Column(db.Boolean(), default=False)
    is_center = Column(db.Boolean(), default=False)
    phone = Column(db.String(30),unique=True)


    integral = Column(db.Integer(),default=0)
    coins = Column(db.Integer(),default=0)

    parent_center = reference_col('users')

    buys_id = relationship('Order', backref='user')
    children_center = relationship("User",join_depth=2,lazy="joined",post_update=True)
    recommends = db.relationship('Recommend',
        foreign_keys=[Recommend.recommender_id],
        backref=db.backref('recommender', lazy='joined'),
        lazy='dynamic',cascade='all, delete-orphan')
    recommender = db.relationship('Recommend',
        foreign_keys=[Recommend.recommends_id],
        backref=db.backref('recommends', lazy='joined'),
        lazy='dynamic',cascade='all, delete-orphan')
    buys_car_id = relationship(BuysCar, backref='users')

    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('roles', lazy='dynamic')
    )



    def __init__(self, username, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username,**kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

    
    def is_administrator(self):
        """管理员"""
        return self.is_admin 


    def init_insert():
        User.create(username='admin', password='aaaaaaaa', active=True)

        
    def generate_auth_token(self, expiration = 600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role
        

from . import login_manager
@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))






