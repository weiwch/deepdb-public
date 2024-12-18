
from schemas.dynamic_single import dynamic_single_table

if __name__ == "__main__":
    sch = dynamic_single_table("t9_100", "../data/tpch100/workload/static/data/{}.csv")
    print(sch.tables[0].attributes)