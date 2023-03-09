"""add content column to posts table

Revision ID: 30e5c3f38a2c
Revises: d8d6c8791e13
Create Date: 2023-03-09 20:09:29.030182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30e5c3f38a2c'
down_revision = 'd8d6c8791e13'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
