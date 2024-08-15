from sqlalchemy import SMALLINT, Column, Integer, String, Boolean, ForeignKey
from models.base_class import Base
from sqlalchemy.orm import relationship


class Category(Base):
      __tablename__ = 'category'
      category_id= Column(SMALLINT(15) , autoincrement=True ,primary_key=True)
      category_name = Column(String(50))
      category_description = Column(String(120))
      category_status = Column(Boolean, default=True)
     