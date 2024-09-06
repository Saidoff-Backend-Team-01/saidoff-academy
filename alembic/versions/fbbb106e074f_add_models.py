"""add models

Revision ID: fbbb106e074f
Revises: 959ef8ed1ce4
Create Date: 2024-09-04 20:05:18.326205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbbb106e074f'
down_revision: Union[str, None] = '959ef8ed1ce4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
