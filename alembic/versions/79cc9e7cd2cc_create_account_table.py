"""create account table

Revision ID: 79cc9e7cd2cc
Revises: 58bc4ffddc14
Create Date: 2024-08-30 20:52:55.727384

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79cc9e7cd2cc'
down_revision: Union[str, None] = '58bc4ffddc14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
