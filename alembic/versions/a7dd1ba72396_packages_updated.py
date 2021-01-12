"""packages updated

Revision ID: a7dd1ba72396
Revises: b0225c6b0392
Create Date: 2021-01-12 03:45:12.852592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7dd1ba72396'
down_revision = 'b0225c6b0392'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Package', sa.Column('all_details', sa.Text(), nullable=False))
    op.add_column('Package', sa.Column('link', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Package', 'link')
    op.drop_column('Package', 'all_details')
    # ### end Alembic commands ###
