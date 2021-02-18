import mysql.connector


def add_filters_into_the_query(sql_query, col_name=""):
    print("add_filters_into_the_query()", sql_query, col_name)
    if col_name:
        sql_query += " WHERE %s = %%s" % col_name
    return sql_query

def add_order_into_the_query(sql_query, order, desc_order):
    if order:
        sql_query += " ORDER BY %s" % order
        if desc_order:
            sql_query += " DESC"
    return sql_query

class MySQL(object):
    def __init__(self):
        self.mydb = self.connect_to_a_database("mydatabase")
        self.mycursor = self.mydb.cursor(buffered=True)
        # self.show_all_databases()
        # self.mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

    def connect_to_a_database(self, database_name=None):
        print("connect_to_a_database()")
        kwargs = {
            "host": "192.168.1.181",
            "user": "root",
            "passwd": "a",
        }
        if database_name:
            kwargs["database"] = database_name
        
        mydb = mysql.connector.connect(**kwargs)
        print(mydb, type(mydb))

        return(mydb)
    
    def show_all(self):
        self.tables = []
        print(self.mycursor)
        for x in self.mycursor:
            print(x)
            self.tables.append(x[0])
        print("self.tables:", self.tables)

    # DATABASES:
    def create_a_new_database(self, database_name):
        self.mycursor.execute("create database %s" % database_name)

    def show_all_databases(self):
        self.mycursor.execute("SHOW DATABASES")
        self.show_all()

    # TABLES:
    # ADD:
    def add_a_table(self, table_name, list_of_fields=["name"]):
        string_with_fields = ""
        for field_name in list_of_fields:
            string_with_fields += ", %s VARCHAR(255)" % field_name
        print("string_with_fields", string_with_fields)
        self.mycursor.execute("CREATE TABLE %s (id INT AUTO_INCREMENT PRIMARY KEY%s)" % (table_name, string_with_fields))

    def add_a_col_into_a_table(self, table_name, col_name, is_primary_key=False):
        if is_primary_key:
            self.mycursor.execute("ALTER TABLE %s ADD COLUMN %s INT AUTO_INCREMENT PRIMARY KEY" % (table_name, col_name))
        else:
            self.mycursor.execute("ALTER TABLE %s ADD COLUMN %s VARCHAR(255)" % (table_name, col_name))

    def add_a_row_into_a_table(self, table_name, cols=(), vals=[]):
        col_names = ""
        form = ""
        for col_name in cols:
            col_names += "%s, " % col_name
            form += "%s, "
        col_names = col_names[:-2]
        form = form[:-2]
        print(col_name, form)
        sql_query = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, col_names, form)
        print(sql_query)
        if len(vals) > 0 and type(vals[0]) != tuple:
            vals = [vals]
        self.mycursor.executemany(sql_query, vals)
        self.mydb.commit()

    # UPDATE:
    def update_a_row_inside_a_table(self, table_name, col_name="", old_name="", new_name=""):
        sql_query = "UPDATE %s SET %s = %%s" % (table_name, col_name)
        print(sql_query)
        # sql_query += " WHERE %s = %%s" % col_name
        sql_query = add_filters_into_the_query(sql_query, col_name)
        print(sql_query)
        self.mycursor.execute(sql_query, (new_name, old_name))
        self.mydb.commit()

    # DELETE:
    def delete_a_table(self, table_name=""):
        print("delete_a_table(table_name=%s)" % table_name)
        self.show_tables()
        print("self.tables:", self.tables)
        if table_name not in self.tables:
            print("please insert a valid name for a table")
            return
        sql_query = "DROP TABLE %s" % table_name
        self.mycursor.execute(sql_query)

    def delete_inside_a_table(self, table_name, filter_query=(), like=False, clear_all=False):
        sql_query = "DELETE FROM %s" % table_name
        if len(filter_query) == 0 and not clear_all:
            print("no changes, because you need to expecify the filter")
            return
        sql_query = add_filters_into_the_query(sql_query, filter_query, like)
        print(sql_query)
        self.mycursor.execute(*sql_query)
        self.mydb.commit()

    # SHOW:
    def show_tables(self):
        self.mycursor.execute("SHOW TABLES")
        self.show_all()

    def show_values_in_a_table(self, table_name, cols=[], one_val=False,
            filter_query=(), like=False,
            order="", desc_order=0):
        print("show_values_in_a_table()", table_name, cols, one_val)
        print("self.mycursor: %s" % self.mycursor)
        if cols:
            cols_to_select = ""
            for col_name in cols:
                cols_to_select += "%s, " % col_name
            cols_to_select = cols_to_select[:-2]
        else:
            cols_to_select = "*"

        sql_query = "select %s from %s" % (cols_to_select, table_name)
        print(sql_query)
        sql_query = add_filters_into_the_query(sql_query, filter_query, like)
        print(sql_query)
        sql_query = add_order_into_the_query(sql_query, order, desc_order)
        print(sql_query, len(sql_query))
        self.mycursor.execute(*sql_query)
        if one_val:
            myresult = self.mycursor.fetchone()
        else:
            myresult = self.mycursor.fetchall()
        print(myresult)

o = MySQL()