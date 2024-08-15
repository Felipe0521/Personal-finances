
from sqlalchemy import Enum ,Float ,Date, CHAR, SMALLINT, Column, Integer, String, Boolean, ForeignKey
from base_class import Base
from sqlalchemy.orm import relationship
import enum

class TransactionType(enum.Enum):
      revenue = "revenue"
      expenses = "expenses"


class Transaction(Base):
      __tablename__ = 'transactions'
      transactions_id= Column(int, autoincrement=True , primary_key=True)
      user_id = Column(CHAR(30), ForeignKey('users.user_id'))
      category_id = Column(Integer(3), ForeignKey('category.category_id'))
      amount = Column(Float(10,2))
      t_description = Column(String(120))
      t_type = Column(Enum(TransactionType))
      t_date = Column(Date)

      user = relationship("User")
      category = relationship("Category")

     