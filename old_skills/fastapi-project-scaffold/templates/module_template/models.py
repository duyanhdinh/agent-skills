from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base


class {{ module_class }}(Base):
    __tablename__ = "{{ module_table }}"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
