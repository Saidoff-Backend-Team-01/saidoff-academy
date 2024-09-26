"""Create a baseline migrations

Revision ID: 0dbc18f1b251
Revises: 
Create Date: 2024-09-26 19:13:31.045174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0dbc18f1b251'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('banner')
    op.drop_table('ourteam')
    op.drop_index('ix_images_id', table_name='images')
    op.drop_table('images')
    op.drop_table('our_services')
    op.drop_table('faq')
    op.drop_table('our_team')
    op.drop_table('why_we_us')
    op.drop_table('services')
    op.drop_table('our_service_info')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('our_service_info',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('additional_info', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['our_services.id'], name='our_service_info_service_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='our_service_info_pkey')
    )
    op.create_table('services',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('desc', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='services_pkey'),
    sa.UniqueConstraint('slug', name='services_slug_key')
    )
    op.create_table('why_we_us',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('desc', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='why_we_us_pkey')
    )
    op.create_table('our_team',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('experience', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='our_team_pkey')
    )
    op.create_table('faq',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('answer', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('faq_type', postgresql.ENUM('GENERAL', 'COMPANY', name='faqtype'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='faq_pkey')
    )
    op.create_table('our_services',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('desc', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='our_services_pkey')
    )
    op.create_table('images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('file_path', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    op.create_index('ix_images_id', 'images', ['id'], unique=False)
    op.create_table('ourteam',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='ourteam_pkey')
    )
    op.create_table('banner',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('desc', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='banner_pkey')
    )
    # ### end Alembic commands ###
