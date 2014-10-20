import sqlite3

DB = None
CONN = None

def get_memory_by_year(year):
	query = """SELECT momAge, annaAge, memory FROM Memories WHERE year = ?"""
	DB.execute(query, (year,))
	row = DB.fetchone()
	return row

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("mombday.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split(',')
        command = tokens[0].strip()
        args = tokens[1:]
        newargs = []
        for arg in args:
            arg = arg.strip()
            newargs.append(arg)

        if command == "get_memory":
            if len(newargs) != 1:
                print "Incorrect number of arguments. This command requires 1 argument: year."
            else:
                get_memory_by_year(*newargs) 
        

    CONN.close()

if __name__ == "__main__":
    main()