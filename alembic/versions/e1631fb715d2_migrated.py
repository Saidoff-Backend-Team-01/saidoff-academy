"""migrated

Revision ID: e1631fb715d2
Revises: 4b18051977ee
Create Date: 2024-09-13 19:36:36.540135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1631fb715d2'
down_revision: Union[str, None] = '4b18051977ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
