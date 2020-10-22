"""Add new account_id and account_email columsn on social account model

Revision ID: 8739603a460f
Revises: df0c688043a1
Create Date: 2020-10-19 21:39:09.598021

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import EmailType


# revision identifiers, used by Alembic.
revision = "8739603a460f"
down_revision = "df0c688043a1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "social_accounts",
        sa.Column("account_email", EmailType(length=255), nullable=True),
    )
    op.add_column(
        "social_accounts", sa.Column("account_id", sa.String(), nullable=True)
    )
    op.create_unique_constraint(
        "uix_email_type", "social_accounts", ["account_email", "account_type"]
    )
    op.create_unique_constraint(
        "uix_id_type", "social_accounts", ["account_id", "account_type"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("uix_id_type", "social_accounts", type_="unique")
    op.drop_constraint("uix_email_type", "social_accounts", type_="unique")
    op.drop_column("social_accounts", "account_id")
    op.drop_column("social_accounts", "account_email")
    # ### end Alembic commands ###