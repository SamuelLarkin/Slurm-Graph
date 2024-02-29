#!/usr/bin/env python3
# \squeue --user=$USER --format='%i,%E,%j,%Z' --noheader | ./graph.py

import shlex
from subprocess import check_output

import click
import networkx as nx

# \squeue --format='%i,%E,%j,%Z'
# 494050,afterok:494013,HoC-CL.Tranlation.016,/gpfs/projects/DT/mtp/models/HoC-ContinualLearning/nmt.hp_search/en2fr/continual_learning.grid.02/lr=3.0e-6_e=64/016

CMD = "squeue --user=$USER --format='%i,%E,%j,%Z' --noheader"
CMD = "squeue --format='%i,%E,%j,%Z' --noheader"


@click.command
def cli():
    graph = nx.Graph()

    job_descriptions = check_output(shlex.split(CMD)).decode("UTF-8")
    job_descriptions = job_descriptions.split()
    job_descriptions = map(str.strip, job_descriptions)
    job_descriptions = map(lambda l: l.split(","), job_descriptions)

    for jobid, dependencies, name, workdir in job_descriptions:
        dependencies = dependencies[len("afterok:") :].split(",")
        graph.add_node(jobid, label=f"{jobid}:{name}:{workdir}")
        for dependency in dependencies:
            graph.add_edge(dependency, jobid)

    nx.write_network_text(graph, with_labels=True)


if __name__ == "__main__":
    cli()
