"""Update transaction_list to MutableList

Revision ID: 9d97316b2b99
Revises: c569c67bd471
Create Date: 2024-07-13 22:02:27.307927

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d97316b2b99'
down_revision: Union[str, None] = 'c569c67bd471'
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