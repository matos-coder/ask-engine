"""conversation + messages

Revision ID: aa4c0dce9b9b
Revises: 593cc6a45ab7
Create Date: 2026-02-04 14:32:04.643313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa4c0dce9b9b'
down_revision: Union[str, Sequence[str], None] = '593cc6a45ab7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
