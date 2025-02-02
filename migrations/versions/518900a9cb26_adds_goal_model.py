"""adds Goal Model

Revision ID: 518900a9cb26
Revises: 35f55aa536f0
Create Date: 2022-05-12 16:14:29.261165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '518900a9cb26'
down_revision = '35f55aa536f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('goal_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goal')
    # ### end Alembic commands ###
