"""add activated_addresses

Revision ID: 1ee76cf990d9
Revises: 43ed89eaa2cb
Create Date: 2014-08-19 17:19:17.289870

"""

# revision identifiers, used by Alembic.
revision = '1ee76cf990d9'
down_revision = '43ed89eaa2cb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'activated_addresses',
        sa.Column('address', sa.String(255), primary_key=True))


def downgrade():
    op.drop_table('activated_addresses')
