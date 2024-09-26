"""test_uchun

Revision ID: 22aed4578261
Revises: 2db70445ca62
Create Date: 2024-09-13 21:37:41.936118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22aed4578261'
down_revision: Union[str, None] = '2db70445ca62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
