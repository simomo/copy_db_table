
def copy(con_src, con_dst, table_name, action='copy', query_sql='', **kwargs):
    '''
    Args
    ----
     * action: could be `copy`, `append`, `upgrade`
        `copy` mode will copy whole table from source db;
        `append` mode will copy new rows from source db and append it to dst db according to the primary key;
        `upgrade` mode need the 'query_sql', it will copy the result of this sql in src db and overwrite to dst db.
    '''
    if not (con_src.open and con_dst.open):
        raise Exception()  # TODO:better message

    if action == 'copy':
        copy_table(con_src, con_dst, table_name, **kwargs)
    elif action == 'append':
        append_table(con_src, con_dst, table_name, **kwargs)
    elif action == 'upgrade':
        upgrade_table(con_src, con_dst, table_name, query_sql='', **kwargs)
    else:
        raise Exception()


def copy_table(con_src, con_dst, table_name, **kwargs):
    pass


def append_table(con_src, con_dst, table_name, **kwargs):
    pass


def upgrade_table(con_src, con_dst, table_name, query_sql='', **kwargs):
    pass
