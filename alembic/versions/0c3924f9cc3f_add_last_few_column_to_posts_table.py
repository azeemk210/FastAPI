"""add last few column to posts table

Revision ID: 0c3924f9cc3f
Revises: 65a74ce11b4f
Create Date: 2025-05-28 23:06:57.970894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c3924f9cc3f'
down_revision: Union[str, None] = '65a74ce11b4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at') 
    """Downgrade schema."""
    pass
