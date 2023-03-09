"""add last few columns to posts table

Revision ID: 99431563ca00
Revises: dc819234a19b
Create Date: 2023-03-09 20:32:48.132494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99431563ca00'
down_revision = 'dc819234a19b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='true'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
