"""create account table

Revision ID: 2acf1af08bbf
Revises: 22aed4578261
Create Date: 2024-09-15 19:37:40.376639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2acf1af08bbf'
down_revision: Union[str, None] = '22aed4578261'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
