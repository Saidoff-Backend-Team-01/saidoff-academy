"""add models

Revision ID: 959ef8ed1ce4
Revises: 58bc4ffddc14
Create Date: 2024-09-04 19:54:43.004302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '959ef8ed1ce4'
down_revision: Union[str, None] = '58bc4ffddc14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
