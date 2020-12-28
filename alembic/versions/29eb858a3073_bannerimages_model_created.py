"""bannerimages model created

Revision ID: 29eb858a3073
Revises: 5cc90cf8fc8d
Create Date: 2020-12-25 22:07:21.092571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29eb858a3073'
down_revision = '5cc90cf8fc8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BannerImgs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_name', sa.String(length=50), nullable=False),
    sa.Column('banner_img', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('BannerImgs')
    # ### end Alembic commands ###