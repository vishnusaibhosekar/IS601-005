import glob
import os



from db import DB
print(os.path.dirname(os.path.abspath(__file__)))
mypath = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(glob.escape(mypath)+"/*.sql")
queries = []

for f in files:
    with open(f, "r") as file:
        queries.append({
            "file": f,
            "sql": file.read()
        })

queries = sorted(queries, key=lambda x:x["file"].lower())

tables = DB.selectAll("SHOW TABLES")
existing_tables = []

if tables.rows:
    for t in tables.rows:
        existing_tables.append(list(t.values())[0])

db_calls = 1
for q in queries:
    sql = q["sql"]
    file = q["file"]
    print(f"Trying file: {file}")
    if "CREATE TABLE" in sql.upper():
        t = sql.split("(")[0] \
        .replace("CREATE TABLE","") \
        .replace("\n","") \
        .strip()
        if t in existing_tables:
            print(f"Table {t} already exists, blocking query")
            continue
    try:
        result = DB.query(sql)
        db_calls += 1
        print(f"Ran {'successfully' if result.status else 'unsuccessfully'}")
    except Exception as e:
        print("An error occurred (some may be expected)", e)
if queries is None:
    queries = []
print(f"Finished running {len(queries)} files")
print(f"Used {db_calls} out of 10000 max quota")
DB.close()
