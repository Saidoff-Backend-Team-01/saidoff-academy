"""create account table

Revision ID: 1e969d0f2efb
Revises: cc68330007ee
Create Date: 2024-09-04 19:41:24.625867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e969d0f2efb'
down_revision: Union[str, None] = 'cc68330007ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
