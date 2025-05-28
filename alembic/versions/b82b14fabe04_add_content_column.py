"""add content column

Revision ID: b82b14fabe04
Revises: 868045839a16
Create Date: 2025-05-28 20:19:30.917907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b82b14fabe04'
down_revision: Union[str, None] = '868045839a16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    """Downgrade schema."""
    pass
