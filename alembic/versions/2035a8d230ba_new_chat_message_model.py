"""new chat message model

Revision ID: 2035a8d230ba
Revises: 119ac0475013
Create Date: 2020-11-15 12:27:56.474816

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = "2035a8d230ba"
down_revision = "119ac0475013"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chat_messages",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("id", UUIDType(binary=False), nullable=False),
        sa.Column("from_user", UUIDType(binary=False), nullable=False),
        sa.Column("to_user", UUIDType(binary=False), nullable=False),
        sa.Column("message", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["from_user"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["to_user"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("chat_messages")
    # ### end Alembic commands ###
