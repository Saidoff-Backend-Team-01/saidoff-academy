"""create account table

Revision ID: 2ad5487b2a61
Revises: 2acf1af08bbf
Create Date: 2024-09-15 22:13:19.394343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ad5487b2a61'
down_revision: Union[str, None] = '2acf1af08bbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
