#!/bin/bash

# tpch
data_path=../data/tpch100/workload/static/data
files=('t0_100.csv' 't14_100.csv' 't16_100.csv' 't1_100.csv' 't21_50.csv' 't22_100.csv' 't2_50.csv' 't4_100.csv' 't5_50.csv' 't6_100.csv' 't9_100.csv')

# STATS
# data_path=../data/STATS/workload/dist_shift/data
# files=('t107_5000.csv' 't108_5000.csv' 't109_5000.csv' 't110_1000.csv' 't112_5000.csv' 't114_1000.csv' 't115_5000.csv' 't116_1000.csv' 't118_5000.csv' 't137_5000.csv' 't138_5000.csv' 't139_5000.csv' 't140_1000.csv' 't147_5000.csv' 't153_10000.csv' 't154_5000.csv' 't189_5000.csv' 't18_5000.csv' 't192_5000.csv' 't1_5000.csv' 't20_5000.csv' 't23_5000.csv' 't32_5000.csv' 't33_5000.csv' 't34_5000.csv' 't35_5000.csv' 't37_5000.csv' 't39_5000.csv' 't40_5000.csv' 't42_5000.csv' 't44_5000.csv' 't46_5000.csv' 't50_1000.csv' 't53_5000.csv' 't60_5000.csv' 't62_5000.csv' 't65_5000.csv' 't68_5000.csv' )


for file in "${files[@]}"; do
  echo $file
  string=$file
  prefix=${string%%_*}
  idx=${prefix:1}
  # echo $idx
  python3 maqp.py --evaluate_aqp_queries \
    --dataset $file \
    --target_path ./res_tpch/q$idx.sql \
    --csv_path $data_path \
    --hdf_path $data_path/gen_hdf_$prefix \
    --ensemble_location $data_path/gen_hdf_$prefix/spn_ensembles/ensemble_single_${file}_10000000.pkl\
    --query_file_location ../data/tpch100/workload/static/query/q${idx}.sql
done
