"""empty message

Revision ID: 8d5dfdd6b6a8
Revises: 
Create Date: 2020-04-09 07:11:55.959362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d5dfdd6b6a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('available', sa.Integer(), nullable=True))
    op.drop_column('tickets', 'attender_email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('attender_email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('tickets', 'available')
    # ### end Alembic commands ###