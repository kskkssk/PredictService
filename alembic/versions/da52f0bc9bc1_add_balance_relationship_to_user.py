"""Add balance relationship to User

Revision ID: da52f0bc9bc1
Revises: 41d8a0eaca78
Create Date: 2024-07-12 16:58:31.813843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da52f0bc9bc1'
down_revision: Union[str, None] = '41d8a0eaca78'
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