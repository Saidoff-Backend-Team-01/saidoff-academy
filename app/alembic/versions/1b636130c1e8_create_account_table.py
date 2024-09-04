"""create account table

Revision ID: 1b636130c1e8
Revises: 94ee2993d9bb
Create Date: 2024-08-31 17:12:40.334160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b636130c1e8'
down_revision: Union[str, None] = '94ee2993d9bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
