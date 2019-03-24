#!/usr/bin/env bash

# change iterations
python -m mcmc.run_mh --iters 100 --save results/mh_100_it_100_var.png --no-show
python -m mcmc.run_mh --iters 500 --save results/mh_500_it_100_var.png --no-show
python -m mcmc.run_mh --iters 1000 --save results/mh_1000_it_100_var.png --no-show
python -m mcmc.run_mh --iters 5000 --save results/mh_5000_it_100_var.png --no-show

# change variance
python -m mcmc.run_mh --iters 5000 --var 0.1 --save results/mh_5000_it_0.1_var.png --no-show
python -m mcmc.run_mh --iters 5000 --var 1 --save results/mh_5000_it_1_var.png --no-show
python -m mcmc.run_mh --iters 5000 --var 1000 --save results/mh_5000_it_1000_var.png --no-show
python -m mcmc.run_mh --iters 5000 --var 2000 --save results/mh_5000_it_2000_var.png --no-show
