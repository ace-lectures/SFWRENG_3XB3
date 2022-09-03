import pyperf  # type: ignore

from mcmath.factorial import fac_acc, fac_acc_oneline, fac_for, fac_rec, fac_rec_oneline, fac_tailrec, fac_tailrec_oneline, fac_while, fac_oneline

from math import factorial

def main():
    ## Benchmark configuration
    functions = [
        factorial, 
        fac_while, fac_for, fac_oneline, fac_rec, fac_rec_oneline,
        fac_acc, fac_acc_oneline,fac_tailrec, fac_tailrec_oneline
    ]
    values = [0, 10, 50, 100, 200, 300]
    ## Running the benchmark
    runner = pyperf.Runner()
    for fac in functions:
        for n in values:
            record = f'{fac.__name__}-{n}'
            runner.bench_func(record, fac, n)
    
if __name__ == "__main__":
    main()