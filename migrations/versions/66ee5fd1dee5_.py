"""empty message

Revision ID: 66ee5fd1dee5
Revises: b5de5bd2c848
Create Date: 2020-04-08 11:46:41.761453

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '66ee5fd1dee5'
down_revision = 'b5de5bd2c848'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_events_end_date_time', table_name='events')
    op.drop_column('events', 'end_date_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('end_date_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_events_end_date_time', 'events', ['end_date_time'], unique=False)
    # ### end Alembic commands ###
