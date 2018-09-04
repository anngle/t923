"""empty message

Revision ID: dc613e9bafc7
Revises: 24aac9510ab3
Create Date: 2018-08-16 21:03:04.911470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc613e9bafc7'
down_revision = '24aac9510ab3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'active_at')
    # ### end Alembic commands ###
