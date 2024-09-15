"""merge heads

Revision ID: 2db70445ca62
Revises: 1e969d0f2efb, 9a9a3d09c0ce, b66da1e577be
Create Date: 2024-09-13 21:37:08.929919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2db70445ca62'
down_revision: Union[str, None] = ('1e969d0f2efb', '9a9a3d09c0ce', 'b66da1e577be')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
