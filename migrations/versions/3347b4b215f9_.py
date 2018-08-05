"""empty message

Revision ID: 3347b4b215f9
Revises: 88cf82c03451
Create Date: 2018-08-05 21:39:12.484693

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3347b4b215f9'
down_revision = '88cf82c03451'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', mysql.VARCHAR(length=80), nullable=True))
    op.create_index('email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###