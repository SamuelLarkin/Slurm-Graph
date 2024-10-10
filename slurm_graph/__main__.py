#!/usr/bin/env python3
# \squeue --user=$USER --format='%i,%E,%j,%Z' --noheader | ./graph.py


import click

# \squeue --format='%i,%E,%j,%Z'
# 494050,afterok:494013,HoC-CL.Tranlation.016,/gpfs/projects/DT/mtp/models/HoC-ContinualLearning/nmt.hp_search/en2fr/continual_learning.grid.02/lr=3.0e-6_e=64/016

CMD = "squeue --format='%i,%E,%j,%Z' --noheader"


@click.command
@click.option(
    "username",
    "-u",
    "--user",
    type=str,
    help="Show tree for a single user",
)
def cli(
    username: str,
):
    import shlex
    from subprocess import check_output

    import networkx as nx

    cmd = CMD
    if username:
        cmd += f" --user={username}"
    job_descriptions = check_output(shlex.split(cmd)).decode("UTF-8")
    job_descriptions = job_descriptions.split()
    job_descriptions = map(str.strip, job_descriptions)
    job_descriptions = map(lambda line: line.split(","), job_descriptions)

    graph = nx.DiGraph()

    root_node = "root_node"
    graph.add_node(root_node, label="all jobs")
    for jobid, dependencies, name, workdir in job_descriptions:
        graph.add_node(jobid, label=f"{jobid}:{name}:{workdir}")
        if dependencies == "(null)":
            graph.add_edge(root_node, jobid)
        else:
            dependencies = dependencies.strip("afterok:").strip("(unfulfilled)")
            dependencies = dependencies.split(",")
            for dependency in dependencies:
                graph.add_edge(dependency, jobid)
                # graph.add_edge(jobid, dependency)

    nx.write_network_text(graph, with_labels=True)


if __name__ == "__main__":
    cli()
