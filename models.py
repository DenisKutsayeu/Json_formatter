from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()


# Определяем модель SQLAlchemy
class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    responsible_user_id = Column(Integer)
    group_id = Column(Integer)
    status_id = Column(Integer)
    pipeline_id = Column(Integer)
    loss_reason_id = Column(Integer)
    created_by = Column(Integer)
    updated_by = Column(Integer)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    closed_at = Column(Integer, nullable=True)
    closest_task_at = Column(Integer, nullable=True)
    is_deleted = Column(Boolean)
    custom_fields = Column(Text)  # Храним JSON в виде текста
    account_id = Column(Integer)
    labor_cost = Column(Float, nullable=True)
