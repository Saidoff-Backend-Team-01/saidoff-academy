"""Create trigger on students table

Revision ID: c0ddb4756287
Revises: 0dbc18f1b251
Create Date: 2024-09-26 19:13:55.928338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0ddb4756287'
down_revision: Union[str, None] = '0dbc18f1b251'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
