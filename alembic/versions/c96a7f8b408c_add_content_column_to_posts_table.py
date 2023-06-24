"""add content column to posts table

Revision ID: c96a7f8b408c
Revises: b21f33e4de04
Create Date: 2023-06-23 11:13:01.093817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c96a7f8b408c'
down_revision = 'b21f33e4de04'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
