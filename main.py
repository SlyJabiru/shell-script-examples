import argparse
import json
from pathlib import Path
import time

# from run_experiment import runner


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get json file containing experiment setup")
    parser.add_argument("--setup", type=str)
    parser.add_argument("--policy", type=str)
    parser.add_argument("--L", type=int)
    args = parser.parse_args()

    setup_file = str(args.setup)
    policy_str = str(args.policy)
    L = int(args.L) if args.L else None
    assert ".json" in setup_file, "setup file name should contain '.json'"

    AVALIABLE_POLICY = [
        'UCB',
        'H_UCB',
        'RH_UCB',
        'Sampled_R_UCB',
    ]
    assert policy_str in AVALIABLE_POLICY, "policy is not available"

    with open(setup_file) as json_file:
        data = json.load(json_file)

        experiment_name = str(Path(setup_file).stem)

        horizon = data["horizon"]
        repetitions = data["repetitions"]
        n_jobs = data["n_jobs"]
        verbosity = data["verbosity"]

        arm_type = data["arm_type"]
        agent_arm_dict = data["agent_arm_dict"]

        save_json = data["save_json"]
        save_h5py = data["save_h5py"]
        save_pickle = data["save_pickle"]

    print(f'policy: {policy_str}')
    print(f'agent_arm_dict: {agent_arm_dict}')
    print()
    time.sleep(3)

    # runner(
    #     experiment_name, policy_str,
    #     horizon, repetitions, n_jobs, verbosity,
    #     arm_type, agent_arm_dict, L,
    #     save_json, save_h5py, save_pickle
    # )