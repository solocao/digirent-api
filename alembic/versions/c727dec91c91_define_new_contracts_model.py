"""Define new contracts model

Revision ID: c727dec91c91
Revises: 8739603a460f
Create Date: 2020-10-23 20:38:29.183400

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType


# revision identifiers, used by Alembic.
revision = "c727dec91c91"
down_revision = "8739603a460f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contracts",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("id", UUIDType(binary=False), nullable=False),
        sa.Column("apartment_application_id", UUIDType(binary=False), nullable=True),
        sa.Column("landlord_has_signed", sa.Boolean(), nullable=False),
        sa.Column("landlord_signed_on", sa.DateTime(), nullable=True),
        sa.Column("tenant_has_signed", sa.Boolean(), nullable=False),
        sa.Column("tenant_signed_on", sa.DateTime(), nullable=True),
        sa.Column("landlord_has_provided_keys", sa.Boolean(), nullable=False),
        sa.Column("landlord_provided_keys_on", sa.DateTime(), nullable=True),
        sa.Column("tenant_has_received_keys", sa.Boolean(), nullable=False),
        sa.Column("tenant_received_keys_on", sa.DateTime(), nullable=True),
        sa.Column("landlord_declined", sa.Boolean(), nullable=False),
        sa.Column("landlord_declined_on", sa.DateTime(), nullable=True),
        sa.Column("tenant_declined", sa.Boolean(), nullable=False),
        sa.Column("tenant_declined_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["apartment_application_id"],
            ["apartment_applications.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "apartment_applications",
        sa.Column("is_considered", sa.Boolean(), nullable=False),
    )
    op.add_column(
        "apartment_applications", sa.Column("is_rejected", sa.Boolean(), nullable=False)
    )
    op.drop_column("apartment_applications", "stage")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "apartment_applications",
        sa.Column("stage", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("apartment_applications", "is_rejected")
    op.drop_column("apartment_applications", "is_considered")
    op.drop_table("contracts")
    # ### end Alembic commands ###