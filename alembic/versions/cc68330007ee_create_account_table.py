"""create account table

Revision ID: cc68330007ee
Revises: 79cc9e7cd2cc
Create Date: 2024-08-30 20:57:59.865365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc68330007ee'
down_revision: Union[str, None] = '79cc9e7cd2cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
