"""Initial migration for creating chat table

Revision ID: 1234567890
Revises: 
Create Date: 2021-10-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1234567890'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'chat',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.String, nullable=False),
        sa.Column('timestamp', sa.DateTime, nullable=False, server_default=sa.func.now())
    )


def downgrade():
    op.drop_table('chat')