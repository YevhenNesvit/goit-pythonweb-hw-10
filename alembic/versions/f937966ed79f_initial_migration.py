"""initial migration

Revision ID: f937966ed79f
Revises: 
Create Date: 2025-01-27 10:41:33.190836

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f937966ed79f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("contacts", "user_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "contacts",
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###
