from pyIpnHeuristic.particleSwarmOptimization import ParticleSwarmOptimization
from pyIpnHeuristic.benchmark import get_pg06


def test_particle_swarm_optimization():
    problem_parameters = get_pg06()

    particle_swarm_optimization = ParticleSwarmOptimization(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=10,
        w=0.15,
        c1=0.2,
        c2=1.5,
        epsilon=10 ** -4
    )

    particle_swarm_optimization.search(iterations=2, save_history=False)

    print(particle_swarm_optimization.population[-1])

    return particle_swarm_optimization.population
