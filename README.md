# Slurm-Graph


## Install

```sh
python -m venv venv
source venv/bin/activate ""
pip install -e .
pip install -e .[dev]
```

or straight from [GitHub](https://github.com/SamuelLarkin/Slurm-Graph)

```sh
pip install git+https://github.com/SamuelLarkin/Slurm-Graph
```


## Running

```sh
slurm-graph
```

```
╙── 492724:HoC-CL.Tranlation.014:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/014
    └── 492687:HoC-CL.Training.014:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/014
        ├──
        │   ├── 504952:bash:/gpfs/home/admin.shengchao.liu/3D_Benchmark_dev_debug/examples_MD
        │   ├── 491840:HoC-CL.Training.016:nmt.hp_search/fr2en/continual_learning.grid.02/lr=1.0e-6_e=128/016
        │   │   ├── 491847:HoC-CL.Tranlation.016:nmt.hp_search/fr2en/continual_learning.grid.02/lr=1.0e-6_e=128/016
        │   │   ├── 491859:HoC-CL.Tranlation.016:nmt.hp_search/fr2en/continual_learning.grid.02/lr=1.0e-6_e=128/016
        │   │   ├── 491862:HoC-CL.Tranlation.016:nmt.hp_search/fr2en/continual_learning.grid.02/lr=1.0e-6_e=128/016
        │   │   └── 492050:HoC-CL.Tranlation.016:nmt.hp_search/fr2en/continual_learning.grid.02/lr=1.0e-6_e=128/016
        │   └── 505006:pca_robust:/gpfs/home/aminm
        ├── 492688:HoC-CL.Tranlation.014:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/014
        ├── 492723:HoC-CL.Tranlation.014:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/014
        └── 492726:HoC-CL.Training.015:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/015
            ├── 492727:HoC-CL.Tranlation.015:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/015
            ├── 492728:HoC-CL.Tranlation.015:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/015
            └── 492765:HoC-CL.Training.016:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/016
                ├── 492766:HoC-CL.Tranlation.016:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/016
                ├── 492801:HoC-CL.Tranlation.016:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/016
                └── 492802:HoC-CL.Tranlation.016:nmt.hp_search/en2fr/continual_learning.grid.02/lr=1.0e-6_e=128/016
```
