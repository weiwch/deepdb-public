import os


# STATS
file = "../data/STATS/workload/dist_shift/workload.sql"
out_fmt = "../data/STATS/workload/dist_shift/query/q{}.sql"
res_fmt = "./res_stats/q{}.sql"
table = ['t107_5000.csv', 't108_5000.csv', 't109_5000.csv', 't110_1000.csv', 't112_5000.csv', 't114_1000.csv', 't115_5000.csv', 't116_1000.csv', 't118_5000.csv', 't137_5000.csv', 't138_5000.csv', 't139_5000.csv', 't140_1000.csv', 't147_5000.csv', 't153_10000.csv', 't154_5000.csv', 't189_5000.csv', 't18_5000.csv', 't192_5000.csv', 't1_5000.csv', 't20_5000.csv', 't23_5000.csv', 't32_5000.csv', 't33_5000.csv', 't34_5000.csv', 't35_5000.csv', 't37_5000.csv', 't39_5000.csv', 't40_5000.csv', 't42_5000.csv', 't44_5000.csv', 't46_5000.csv', 't50_1000.csv', 't53_5000.csv', 't60_5000.csv', 't62_5000.csv', 't65_5000.csv', 't68_5000.csv' ]
out_final = "stats_static_result.sql"
trm_idx = 226


# # tpch
# file = "../data/tpch100/workload/static/workload.sql"
# out_fmt = "../data/tpch100/workload/static/query/q{}.sql"
# res_fmt = "./res_tpch/q{}.sql"
# table = ['t0_100.csv',, 't14_100.csv',, 't16_100.csv',, 't1_100.csv',, 't21_50.csv',, 't22_100.csv',, 't2_50.csv',, 't4_100.csv',, 't5_50.csv',, 't6_100.csv',, 't9_100.csv',,]
# out_final = "tpch_static_result.sql"
# trm_idx = 58


idx = [x.split("_")[0][1:] for x in table]
print(idx)
fp_list = []
for i in range(trm_idx):
    if str(i) in idx:
        fp = open(res_fmt.format(i), "r")
    else:
        fp = open(out_fmt.format(i), "r")
    fp_list.append(fp)

with open(out_final, "w") as out:
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            id, sql = line.split(":")
            id = int(id.strip())
            res = fp_list[id].readline()
            print(res)
            out.write(res)

for f in fp_list:
    f.close()
        
    