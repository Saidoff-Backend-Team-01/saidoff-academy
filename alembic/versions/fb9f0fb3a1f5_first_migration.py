"""First migration

Revision ID: fb9f0fb3a1f5
Revises: 70112a61a802
Create Date: 2024-09-15 17:41:07.121797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType


# revision identifiers, used by Alembic.
revision: str = 'fb9f0fb3a1f5'
down_revision: Union[str, None] = '70112a61a802'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banner',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('bg_image', ImageType(storage=FileSystemStorage(path='tmp/')), nullable=True),
    sa.Column('phone_num', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_with_us',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('faq',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('faq_type', sa.Enum('GENERAL', 'COMPANY', name='faqtype'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedbacks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('feedback_text', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('our_services',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('our_team',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('position', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('experience', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('button_text', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('social_medias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sponsors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('why_we_us',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('bg_image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('our_service_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('additional_info', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['our_services.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['portfolio_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio_item')
    op.drop_table('portfolio_category')
    op.drop_table('our_service_info')
    op.drop_table('why_we_us')
    op.drop_table('sponsors')
    op.drop_table('social_medias')
    op.drop_table('portfolio')
    op.drop_table('our_team')
    op.drop_table('our_services')
    op.drop_table('feedbacks')
    op.drop_table('faq')
    op.drop_table('contact_with_us')
    op.drop_table('banner')
    # ### end Alembic commands ###
