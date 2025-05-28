"""add foreign key to posts table

Revision ID: 65a74ce11b4f
Revises: 44a352bb5ec8
Create Date: 2025-05-28 20:29:38.429972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65a74ce11b4f'
down_revision: Union[str, None] = '44a352bb5ec8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column(
            'owner_id',
            sa.Integer,
            nullable=False
        )
    )
    op.create_foreign_key(
        'posts_users_fk', source_table='posts', referent_table='users',
        local_cols=['owner_id'],
        remote_cols= ['id'],
        ondelete='CASCADE'
    )
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    """Downgrade schema."""
    pass
