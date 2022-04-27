"""Three

Revision ID: 2e1e361a461f
Revises: 71397d90e6b7
Create Date: 2022-04-28 02:46:54.914061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e1e361a461f'
down_revision = '71397d90e6b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('table_product', sa.Column('table_id', sa.Integer(), nullable=True))
    op.drop_constraint('table_product_table_fkey', 'table_product', type_='foreignkey')
    op.create_foreign_key(None, 'table_product', 'table', ['table_id'], ['id'])
    op.drop_column('table_product', 'table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('table_product', sa.Column('table', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'table_product', type_='foreignkey')
    op.create_foreign_key('table_product_table_fkey', 'table_product', 'table', ['table'], ['id'])
    op.drop_column('table_product', 'table_id')
    # ### end Alembic commands ###