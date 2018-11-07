"""empty message

Revision ID: e0a5da4798cf
Revises: d1e988a3cd2f
Create Date: 2018-10-28 12:44:19.206382

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e0a5da4798cf'
down_revision = 'd1e988a3cd2f'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('categorys', sa.Column('parent_id', sa.Integer(), nullable=True))
    # op.create_foreign_key(None, 'categorys', 'categorys', ['parent_id'], ['id'])
    # op.add_column('products', sa.Column('active', sa.Boolean(), nullable=True))
    # op.add_column('products', sa.Column('attach_key', sa.String(length=500), nullable=True))
    # op.add_column('products', sa.Column('attach_value', sa.String(length=500), nullable=True))
    # op.add_column('products', sa.Column('buy_count', sa.Integer(), nullable=True))
    # op.add_column('products', sa.Column('click_count', sa.Integer(), nullable=True))
    # op.add_column('products', sa.Column('created_at', sa.DateTime(), nullable=False))
    # op.add_column('products', sa.Column('ean', sa.String(length=50), nullable=True))
    # op.add_column('products', sa.Column('hot', sa.Boolean(), nullable=True))
    # op.add_column('products', sa.Column('is_sell', sa.Boolean(), nullable=True))
    # op.add_column('products', sa.Column('main_photo', sa.String(length=200), nullable=True))
    # op.add_column('products', sa.Column('note', sa.UnicodeText(), nullable=True))
    # op.add_column('products', sa.Column('special_price', sa.Numeric(precision=10, scale=2), nullable=True))
    # op.add_column('products', sa.Column('unit', sa.Integer(), nullable=True))
    # op.drop_column('products', 'thumbnail')
    # op.add_column('users', sa.Column('coins', sa.Integer(), nullable=True))
    # op.add_column('users', sa.Column('integral', sa.Integer(), nullable=True))
    # # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'integral')
    op.drop_column('users', 'coins')
    op.add_column('products', sa.Column('thumbnail', mysql.VARCHAR(length=200), nullable=True))
    op.drop_column('products', 'unit')
    op.drop_column('products', 'special_price')
    op.drop_column('products', 'note')
    op.drop_column('products', 'main_photo')
    op.drop_column('products', 'is_sell')
    op.drop_column('products', 'hot')
    op.drop_column('products', 'ean')
    op.drop_column('products', 'created_at')
    op.drop_column('products', 'click_count')
    op.drop_column('products', 'buy_count')
    op.drop_column('products', 'attach_value')
    op.drop_column('products', 'attach_key')
    op.drop_column('products', 'active')
    op.drop_constraint(None, 'categorys', type_='foreignkey')
    op.drop_column('categorys', 'parent_id')
    # ### end Alembic commands ###