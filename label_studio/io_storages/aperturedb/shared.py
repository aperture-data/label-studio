from io_storages.aperturedb.connection_pool import ConnectionPool
from aperturedb.Connector import Connector

pool_group = dict()
def get_pool_by_key( aperturedb_key ):
    def map_key_to_connector():
        db = Connector( key=aperturedb_key )
        db.use_keepalive = True
        return db

    if not aperturedb_key in pool_group:
        pool_group[aperturedb_key] = ConnectionPool( connection_factory = map_key_to_connector )
    return pool_group[aperturedb_key]
