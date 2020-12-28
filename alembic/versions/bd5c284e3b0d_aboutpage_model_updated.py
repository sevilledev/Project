"""aboutpage model updated

Revision ID: bd5c284e3b0d
Revises: 9fc8a3e26c7e
Create Date: 2020-12-27 14:58:03.480872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5c284e3b0d'
down_revision = '9fc8a3e26c7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('AboutPage', 'main_text',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('AboutPage', 'second_img',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('AboutPage', 'second_img',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('AboutPage', 'main_text',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###