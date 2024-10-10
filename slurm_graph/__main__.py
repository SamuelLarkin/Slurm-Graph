#!/usr/bin/env python3
# \squeue --user=$USER --format='%i,%E,%j,%Z' --noheader | ./graph.py


import click

# \squeue --format='%i,%E,%j,%Z'
# 494050,afterok:494013,HoC-CL.Tranlation.016,/gpfs/projects/DT/mtp/models/HoC-ContinualLearning/nmt.hp_search/en2fr/continual_learning.grid.02/lr=3.0e-6_e=64/016

CMD = "squeue --format='%i,%E,%j,%Z' --noheader"

from dataclasses import dataclass


@dataclass(frozen=False)
class Job:
    """
    Job description.
    """

    id: int
    name: str
    workdir: str = None
    dependencies: set[int] = frozenset()
    num_dependent: int = 0

    def __str__(self) -> str:
        if self.workdir:
            return f"({self.num_dependent}): {self.id}:{self.name}:{self.workdir}"
        else:
            # This is the root node
            return f"({self.num_dependent}): {self.name}"

    def __hash__(self):
        return hash(str(self.id))

    @classmethod
    def from_description(cls, line: str):
        jobid, dependencies, name, workdir = line.strip().split(",")
        if dependencies == "(null)":
            dependencies = []
        else:
            dependencies = dependencies.strip("afterok:").strip("(unfulfilled)")
            dependencies = map(int, dependencies.split(","))
        return cls(
            id=int(jobid),
            dependencies=frozenset(dependencies),
            name=name,
            workdir=workdir,
        )


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
    """
    Display a SLURM's job dependency graph.
    """
    import shlex
    from subprocess import check_output

    import networkx as nx

    cmd = CMD
    if username:
        cmd += f" --user={username}"

    job_descriptions = check_output(shlex.split(cmd)).decode("UTF-8").splitlines()
    jobs = [Job.from_description(description) for description in job_descriptions]

    graph = nx.DiGraph()

    nodes = {job.id: job for job in jobs}
    root_node = Job(id=0, name="all jobs")
    nodes[root_node.id] = root_node
    for node in nodes.values():
        graph.add_node(node)

    for job in jobs:
        if job.dependencies:
            for dependency in job.dependencies:
                graph.add_edge(nodes[dependency], nodes[job.id])
                nodes[dependency].num_dependent += 1
        else:
            graph.add_edge(root_node, nodes[job.id])
            root_node.num_dependent += 1

    nx.write_network_text(graph, with_labels=True)


if __name__ == "__main__":
    cli()
