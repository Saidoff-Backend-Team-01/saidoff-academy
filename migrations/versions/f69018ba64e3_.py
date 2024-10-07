"""empty message

Revision ID: f69018ba64e3
Revises: 90cd95fbc127
Create Date: 2024-10-02 17:27:52.462396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f69018ba64e3'
down_revision: Union[str, None] = '90cd95fbc127'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
