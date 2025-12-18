from app.core.db import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy import String, DateTime, Integer, ForeignKey, Column, Boolean, Text, func
from datetime import datetime, timezone
from app.user.model.user_model import User


class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    owner: Mapped["User"] = relationship(back_populates="todos")

# id SERIAL PRIMARY KEY,
# title VARCHAR(200) NOT NULL,
# description TEXT,
# completed BOOLEAN DEFAULT false,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE