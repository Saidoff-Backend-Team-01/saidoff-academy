"""create account table

Revision ID: 9a9a3d09c0ce
Revises: 58bc4ffddc14
Create Date: 2024-08-30 16:09:45.108229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a9a3d09c0ce'
down_revision: Union[str, None] = '58bc4ffddc14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
