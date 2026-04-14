from __future__ import annotations

from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

# Replace with your own models/session wiring.
from app.core.db import SessionLocal
from app.features.common.models import LookupValue


def upsert_lookup_values(db: Session, items: Iterable[dict]) -> None:
    for item in items:
        key = item["key"]
        stmt = select(LookupValue).where(LookupValue.key == key)
        existing = db.execute(stmt).scalar_one_or_none()
        if existing is None:
            db.add(LookupValue(**item))
        else:
            existing.value = item["value"]
            existing.is_active = item.get("is_active", True)


def run_seed() -> None:
    seed_rows = [
        {"key": "role_admin", "value": "Administrator", "is_active": True},
        {"key": "role_user", "value": "User", "is_active": True},
    ]

    db = SessionLocal()
    try:
        upsert_lookup_values(db, seed_rows)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
