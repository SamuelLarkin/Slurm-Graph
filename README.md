# Slurm-Graph

Display SLURM's job dependencies as a graph.

## Install

```sh
python -m venv venv
source venv/bin/activate ""
pip install -e .
pip install -e .[dev]
```

or straight from [GitHub](https://github.com/SamuelLarkin/Slurm-Graph)

```sh
python -m pip install git+https://github.com/SamuelLarkin/Slurm-Graph
```

### One file

[PyInstaller Manual](https://pyinstaller.org/en/stable/index.html)
Install `slurm-graph` as a one binary file.

```sh
python -m venv venv
source venv/bin/activate ""
python -m pip install .[install]
pyinstaller --onefile venv/bin/slurm-graph
install dist/slurm-graph ~/.local/bin/
```

## Running

```sh
slurm-graph
```

```
╙── (2): all jobs
    ├─╼ (19): 71347:HoC-Senate.training:/models/HoC-Senate/nmt/en2fr/baseline-2024-10
    │   ├─╼ (0): 72201:SenateC-fine-1:/models/Senate-2023/nmt/Committees/en2fr.2024-10/finetuning/1
    │   ├─╼ (0): 72200:SenateC-fine-2:/models/Senate-2023/nmt/Committees/en2fr.2024-10/finetuning/2
    │   ├─╼ (0): 72199:SenateC-fine-3:/models/Senate-2023/nmt/Committees/en2fr.2024-10/finetuning/3
    │   ├─╼ (3): 72198:SenateC-fine-4:/models/Senate-2023/nmt/Committees/en2fr.2024-10/finetuning/4
    │   │   ├─╼ (0): 72204:SenateC-rece-setup03.train:/models/Senate-2023/nmt/Committees/en2fr.2024-10/recency/setup03
    │   │   ├─╼ (0): 72203:SenateC-rece-setup02.train:/models/Senate-2023/nmt/Committees/en2fr.2024-10/recency/setup02
    │   │   └─╼ (0): 72202:SenateC-rece-setup01.train:/models/Senate-2023/nmt/Committees/en2fr.2024-10/recency/setup01
    │   ├─╼ (0): 72197:SenateC-fine-5:/models/Senate-2023/nmt/Committees/en2fr.2024-10/finetuning/5
    │   ├─╼ (0): 72196:SenateC-fine-6:/models/Senate-2023/nmt/Committees/en2fr.2024-10/finetuning/6
    │   ├─╼ (0): 72183:SenateD-fine-1:/models/Senate-2023/nmt/Debates/en2fr.2024-10/finetuning/1
    │   ├─╼ (3): 72182:SenateD-fine-2:/models/Senate-2023/nmt/Debates/en2fr.2024-10/finetuning/2
    │   │   ├─╼ (0): 72186:SenateD-rece-setup03.train:/models/Senate-2023/nmt/Debates/en2fr.2024-10/recency/setup03
    │   │   ├─╼ (0): 72185:SenateD-rece-setup02.train:/models/Senate-2023/nmt/Debates/en2fr.2024-10/recency/setup02
    │   │   └─╼ (0): 72184:SenateD-rece-setup01.train:/models/Senate-2023/nmt/Debates/en2fr.2024-10/recency/setup01
    │   ├─╼ (0): 72181:SenateD-fine-3:/models/Senate-2023/nmt/Debates/en2fr.2024-10/finetuning/3
    │   ├─╼ (0): 72180:SenateD-fine-4:/models/Senate-2023/nmt/Debates/en2fr.2024-10/finetuning/4
    │   ├─╼ (0): 72179:SenateD-fine-5:/models/Senate-2023/nmt/Debates/en2fr.2024-10/finetuning/5
    │   ├─╼ (0): 72178:SenateD-fine-6:/models/Senate-2023/nmt/Debates/en2fr.2024-10/finetuning/6
    │   ├─╼ (0): 72169:HoCC-fine-1:/models/HoC-Committees/nmt/xml/en2fr.2024-10/finetuning/1
    │   ├─╼ (3): 72168:HoCC-fine-2:/models/HoC-Committees/nmt/xml/en2fr.2024-10/finetuning/2
    │   │   ├─╼ (0): 72172:HoCC-rece-setup03.train:/models/HoC-Committees/nmt/xml/en2fr.2024-10/recency/setup03
    │   │   ├─╼ (0): 72171:HoCC-rece-setup02.train:/models/HoC-Committees/nmt/xml/en2fr.2024-10/recency/setup02
    │   │   └─╼ (0): 72170:HoCC-rece-setup01.train:/models/HoC-Committees/nmt/xml/en2fr.2024-10/recency/setup01
    │   ├─╼ (0): 72167:HoCC-fine-3:/models/HoC-Committees/nmt/xml/en2fr.2024-10/finetuning/3
    │   ├─╼ (0): 72140:HoCD-fine-1:/models/HoC-Debates/nmt/xml/en2fr.2024-10/finetuning/1
    │   ├─╼ (0): 72139:HoCD-fine-2:/models/HoC-Debates/nmt/xml/en2fr.2024-10/finetuning/2
    │   ├─╼ (0): 72138:HoCD-fine-3:/models/HoC-Debates/nmt/xml/en2fr.2024-10/finetuning/3
    │   └─╼ (3): 72137:HoCD-fine-4:/models/HoC-Debates/nmt/xml/en2fr.2024-10/finetuning/4
    │       ├─╼ (0): 72143:HoCD-rece-setup02.train:/models/HoC-Debates/nmt/xml/en2fr.2024-10/recency/setup02
    │       ├─╼ (0): 72142:HoCD-rece-setup03.train:/models/HoC-Debates/nmt/xml/en2fr.2024-10/recency/setup03
    │       └─╼ (0): 72141:HoCD-rece-setup01.train:/models/HoC-Debates/nmt/xml/en2fr.2024-10/recency/setup01
    └─╼ (18): 71346:HoC-Senate.training:/models/HoC-Senate/nmt/fr2en/baseline-2024-10
        ├─╼ (0): 72219:SenateC-fine-1:/models/Senate-2023/nmt/Committees/fr2en.2024-10/finetuning/1
        ├─╼ (0): 72218:SenateC-fine-2:/models/Senate-2023/nmt/Committees/fr2en.2024-10/finetuning/2
        ├─╼ (2): 72217:SenateC-fine-3:/models/Senate-2023/nmt/Committees/fr2en.2024-10/finetuning/3
        │   ├─╼ (0): 72221:SenateC-rece-setup01.train:/models/Senate-2023/nmt/Committees/fr2en.2024-10/recency/setup01
        │   └─╼ (0): 72220:SenateC-rece-setup03.train:/models/Senate-2023/nmt/Committees/fr2en.2024-10/recency/setup03
        ├─╼ (0): 72216:SenateC-fine-4:/models/Senate-2023/nmt/Committees/fr2en.2024-10/finetuning/4
        ├─╼ (0): 72215:SenateC-fine-5:/models/Senate-2023/nmt/Committees/fr2en.2024-10/finetuning/5
        ├─╼ (0): 72214:SenateC-fine-6:/models/Senate-2023/nmt/Committees/fr2en.2024-10/finetuning/6
        ├─╼ (0): 72192:SenateD-fine-1:/models/Senate-2023/nmt/Debates/fr2en.2024-10/finetuning/1
        ├─╼ (0): 72191:SenateD-fine-2:/models/Senate-2023/nmt/Debates/fr2en.2024-10/finetuning/2
        ├─╼ (0): 72190:SenateD-fine-3:/models/Senate-2023/nmt/Debates/fr2en.2024-10/finetuning/3
        ├─╼ (0): 72189:SenateD-fine-4:/models/Senate-2023/nmt/Debates/fr2en.2024-10/finetuning/4
        ├─╼ (0): 72188:SenateD-fine-5:/models/Senate-2023/nmt/Debates/fr2en.2024-10/finetuning/5
        ├─╼ (3): 72187:SenateD-fine-6:/models/Senate-2023/nmt/Debates/fr2en.2024-10/finetuning/6
        │   ├─╼ (0): 72195:SenateD-rece-setup03.train:/models/Senate-2023/nmt/Debates/fr2en.2024-10/recency/setup03
        │   ├─╼ (0): 72194:SenateD-rece-setup02.train:/models/Senate-2023/nmt/Debates/fr2en.2024-10/recency/setup02
        │   └─╼ (0): 72193:SenateD-rece-setup01.train:/models/Senate-2023/nmt/Debates/fr2en.2024-10/recency/setup01
        ├─╼ (0): 72174:HoCC-fine-1:/models/HoC-Committees/nmt/xml/fr2en.2024-10/finetuning/1
        ├─╼ (3): 72173:HoCC-fine-2:/models/HoC-Committees/nmt/xml/fr2en.2024-10/finetuning/2
        │   ├─╼ (0): 72177:HoCC-rece-setup03.train:/models/HoC-Committees/nmt/xml/fr2en.2024-10/recency/setup03
        │   ├─╼ (0): 72176:HoCC-rece-setup02.train:/models/HoC-Committees/nmt/xml/fr2en.2024-10/recency/setup02
        │   └─╼ (0): 72175:HoCC-rece-setup01.train:/models/HoC-Committees/nmt/xml/fr2en.2024-10/recency/setup01
        ├─╼ (0): 72147:HoCD-fine-3:/models/HoC-Debates/nmt/xml/fr2en.2024-10/finetuning/3
        ├─╼ (3): 72146:HoCD-fine-4:/models/HoC-Debates/nmt/xml/fr2en.2024-10/finetuning/4
        │   ├─╼ (0): 72150:HoCD-rece-setup03.train:/models/HoC-Debates/nmt/xml/fr2en.2024-10/recency/setup03
        │   ├─╼ (0): 72149:HoCD-rece-setup02.train:/models/HoC-Debates/nmt/xml/fr2en.2024-10/recency/setup02
        │   └─╼ (0): 72148:HoCD-rece-setup01.train:/models/HoC-Debates/nmt/xml/fr2en.2024-10/recency/setup01
        ├─╼ (0): 72145:HoCD-fine-5:/models/HoC-Debates/nmt/xml/fr2en.2024-10/finetuning/5
        └─╼ (0): 72144:HoCD-fine-6:/models/HoC-Debates/nmt/xml/fr2en.2024-10/finetuning/6
```
