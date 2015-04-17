"""empty message

Revision ID: 59bca7238b7
Revises: 436c14e3529
Create Date: 2015-04-17 12:46:26.708422

"""

# revision identifiers, used by Alembic.
revision = '59bca7238b7'
down_revision = '436c14e3529'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('_avatar', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('description', sa.Text(), nullable=True))
    op.drop_constraint('avatar_storage', 'users', type_='foreignkey')
    op.drop_column('users', 'avatar_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('avatar_storage', 'users', 'image_store', ['avatar_id'], ['id'])
    op.drop_column('users', 'description')
    op.drop_column('users', '_avatar')
    ### end Alembic commands ###
