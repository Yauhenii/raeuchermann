from typing import List

from pydantic import parse_obj_as

from app.db.basic_handler import BasicHandler
from app.db.utils import unpack_entity
from app.model import Entity


class EntityHandler(BasicHandler):
    INSERT_ENTITY_QUERY = """
    INSERT INTO {} 
    (e_name, e_number, e_date) 
    VALUES (%s,%s,%s)
    """

    def insert_entity(self, args) -> Entity:
        self.execute(EntityHandler.INSERT_ENTITY_QUERY, args)
        return unpack_entity(args)

    SELECT_ENTITY_BY_NAME = """
    SELECT * FROM {}
    WHERE e_name=%s
    """

    def select_entity_by_name(self, args) -> List[Entity]:
        result = self.execute(EntityHandler.SELECT_ENTITY_BY_NAME, args)
        entity_list = []
        for row in result:
            entity_list.append(unpack_entity(row, index_shift=True))
        if len(entity_list) == 0:
            raise IndexError
        return parse_obj_as(List[Entity], entity_list)
