"""Add user, balance, request tables

Revision ID: 59bd435adf0d
Revises: 7baeddd46491
Create Date: 2024-07-23 07:06:53.835854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59bd435adf0d'
down_revision: Union[str, None] = '7baeddd46491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###