"""create account table

Revision ID: b44480ce2a00
Revises: 2ad5487b2a61
Create Date: 2024-09-15 22:15:55.467306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b44480ce2a00'
down_revision: Union[str, None] = '2ad5487b2a61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
