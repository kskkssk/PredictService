"""Fix transaction_list default

Revision ID: c602c4bd198e
Revises: 10d1eeaa605d
Create Date: 2024-07-13 21:41:58.520497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c602c4bd198e'
down_revision: Union[str, None] = '10d1eeaa605d'
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