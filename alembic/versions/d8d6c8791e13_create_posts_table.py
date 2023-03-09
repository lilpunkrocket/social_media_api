"""create posts table

Revision ID: d8d6c8791e13
Revises: 
Create Date: 2023-03-09 19:59:20.209722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8d6c8791e13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                             sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
