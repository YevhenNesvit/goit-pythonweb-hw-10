"""add auth

Revision ID: 9b4641dcaa8c
Revises: f937966ed79f
Create Date: 2025-01-27 11:14:48.568624

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9b4641dcaa8c"
down_revision: Union[str, None] = "f937966ed79f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("contacts", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "contacts", "users", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "contacts", type_="foreignkey")
    op.drop_column("contacts", "user_id")
    # ### end Alembic commands ###
