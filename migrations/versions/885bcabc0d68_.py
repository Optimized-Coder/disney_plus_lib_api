"""empty message

Revision ID: 885bcabc0d68
Revises: 2287956b598f
Create Date: 2023-04-21 20:20:29.501847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '885bcabc0d68'
down_revision = '2287956b598f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.alter_column('img_url',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.alter_column('img_url',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
