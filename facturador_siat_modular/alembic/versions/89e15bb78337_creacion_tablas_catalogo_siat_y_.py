"""creacion_tablas_catalogo_siat_y_actualizacion_fks

Revision ID: 89e15bb78337
Revises: 2cca4027c43a
Create Date: 2025-06-01 05:45:54.661168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89e15bb78337'
down_revision: Union[str, None] = '2cca4027c43a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
