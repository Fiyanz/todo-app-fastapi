from sqlalchemy.testing.schema import mapped_column
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Integer, String, DateTime, Boolean
from typing import List
from app.core.db import Base

from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[Boolean] = mapped_column(Boolean, default=True, nullable=True)
    last_login: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    todos: Mapped[List["Todo"]] = relationship(back_populates="owner")

# id SERIAL PRIMARY KEY,
# username VARCHAR(50) UNIQUE NOT NULL,
# email VARCHAR(100) UNIQUE NOT NULL,
# hashed_password VARCHAR(255) NOT NULL,
# full_name VARCHAR(100),
# is_active BOOLEAN DEFAULT true,
# last_login TIMESTAMP,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

