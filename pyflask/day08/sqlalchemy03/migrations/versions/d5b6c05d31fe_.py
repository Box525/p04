"""empty message

Revision ID: d5b6c05d31fe
Revises: 
Create Date: 2019-03-13 22:58:23.044656

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5b6c05d31fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cname', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('student')
    op.drop_table('score')
    op.drop_table('grade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('gid', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('gname', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('score',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cname', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('sc', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('student',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sid', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('sname', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('gid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['grade.id'], name='student_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('car')
    # ### end Alembic commands ###
