"""new looking for model

Revision ID: b079c5571a43
Revises: cefa26545898
Create Date: 2020-09-29 20:12:42.917905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType, ChoiceType
from digirent.database.enums import HouseType

# revision identifiers, used by Alembic.
revision = "b079c5571a43"
down_revision = "cefa26545898"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "looking_for",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("id", UUIDType(binary=False), nullable=False),
        sa.Column("user_id", UUIDType(binary=False), nullable=True),
        sa.Column(
            "house_type", ChoiceType(HouseType, impl=sa.String()), nullable=False
        ),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("max_budget", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("looking_for")
    # ### end Alembic commands ###
