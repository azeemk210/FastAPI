"""add user table

Revision ID: 44a352bb5ec8
Revises: b82b14fabe04
Create Date: 2025-05-28 20:23:07.319198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44a352bb5ec8'
down_revision: Union[str, None] = 'b82b14fabe04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('users')
    """Downgrade schema."""
    pass
