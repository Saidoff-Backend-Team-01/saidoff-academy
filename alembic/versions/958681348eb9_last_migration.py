"""Last migration

Revision ID: 958681348eb9
Revises: e5895a2b9c4e
Create Date: 2024-09-20 13:49:38.703571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

# revision identifiers, used by Alembic.
revision: str = '958681348eb9'
down_revision: Union[str, None] = 'e5895a2b9c4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('our_team',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('position', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', ImageType(storage=FileSystemStorage(path='tmp/')), nullable=False),
    sa.Column('experience', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('our_team')
    # ### end Alembic commands ###
