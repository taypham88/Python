'''Database model for social network'''

# pylint: disable=R0903
from pathlib import Path
import peewee as pw


HERE = Path(__file__).parent

def start_database(filename='social.db', clear=False):
    """
    initialize an empty databse
    """
    models = [UsersTable, StatusTable]
    d_b = get_database(filename, clear)
    d_b.bind(models,
            bind_refs=False,
            bind_backrefs=False)
    d_b.connect()
    d_b.create_tables(models)

    return d_b

def get_database(filename=None, clear=False, default_db='social.db'):
    """
    setup and return a database to use for the models

    :param filename: name of DB file, or ":memory:" for in=memory temp DB

    :param clear=False: Whether to clear out the old db and return an
                        empty one.
    """

    if filename == ":memory:":
        d_b = pw.SqliteDatabase(':memory:',
                                pragmas={'foreign_keys': 1}
                               )

    else:
        if filename is None:
            filename = default_db
        if clear:
            Path(filename).unlink(missing_ok=True)
        d_b = pw.SqliteDatabase(HERE / filename,
                               pragmas={'foreign_keys': 1}
                               )
    return d_b

class BaseModel(pw.Model):
    '''BaseModel for database'''

    class Meta:
        '''Database Meta, note this is what peewee bindings does'''

        database = get_database(":memory:")

class UsersTable(BaseModel):
    '''User BadeModel to populate database fields'''

    user_id = pw.CharField(primary_key = True, max_length = 30)
    user_name = pw.CharField(max_length = 30)
    user_last_name = pw.CharField(max_length = 100)
    email = pw.CharField()

class StatusTable(BaseModel):
    '''Status BadeModel to populate database fields'''

    status_id = pw.CharField(primary_key=True, max_length=30)
    user_id = pw.ForeignKeyField(model=UsersTable,
                                 field='user_id',
                                 backref='status_messages',
                                 on_delete='CASCADE')
    status_text = pw.TextField()
