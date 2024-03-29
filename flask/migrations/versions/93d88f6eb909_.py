"""empty message

Revision ID: 93d88f6eb909
Revises: 
Create Date: 2023-05-09 17:02:21.333087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93d88f6eb909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('checkin', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.TEXT(length=100),
               type_=sa.String(length=100),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.TEXT(length=100),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.TEXT(length=15),
               type_=sa.String(length=15),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.TEXT(length=100),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(length=100),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=15),
               type_=sa.TEXT(length=15),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(length=100),
               existing_nullable=False)

    with op.batch_alter_table('checkin', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
