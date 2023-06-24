"""add user table

Revision ID: 572e67def885
Revises: c96a7f8b408c
Create Date: 2023-06-23 11:26:00.332169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '572e67def885'
down_revision = 'c96a7f8b408c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
