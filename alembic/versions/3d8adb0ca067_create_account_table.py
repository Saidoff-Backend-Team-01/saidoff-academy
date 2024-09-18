"""create account table

Revision ID: 3d8adb0ca067
Revises: 1b636130c1e8
Create Date: 2024-09-06 20:09:34.602038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d8adb0ca067'
down_revision: Union[str, None] = '1b636130c1e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
