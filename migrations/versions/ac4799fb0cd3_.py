"""empty message

Revision ID: ac4799fb0cd3
Revises: 3b042c12d85e
Create Date: 2018-12-12 22:47:40.070151

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ac4799fb0cd3'
down_revision = '3b042c12d85e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles_parents',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], )
    )
    op.create_table('users_roles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.drop_table('sysconfig')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sysconfig',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('web_name', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('web_describe', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('user_register', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('active_site', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('close_register_user_message', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('close_website_message', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('withdraw_money', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('users_roles')
    op.drop_table('roles_parents')
    op.drop_table('roles')
    # ### end Alembic commands ###