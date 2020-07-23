"""Update pitch and user classes

Revision ID: f6893ba0692f
Revises: 0000b85fa4c9
Create Date: 2020-07-19 13:47:29.939109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6893ba0692f'
down_revision = '0000b85fa4c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('time', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_code', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'pass_code')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    op.drop_column('pitches', 'time')
    # ### end Alembic commands ###
