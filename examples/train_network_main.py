
import os
import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig
from ray.tune.registry import register_env
import or_gym
import matplotlib.pyplot as plt
import numpy as np

# Function to register the environment
def register_or_gym_env(env_name, env_config={}):
    def env_creator(config):
        return or_gym.make(env_name, env_config=config)
    register_env(env_name, env_creator)

def train_and_plot():
    # 1. Initialize Ray
    ray.init(ignore_reinit_error=True)

    # 2. Register Environment
    env_name = "NetworkManagement-v1"
    register_or_gym_env(env_name)

    # 3. Configure PPO
    config = (
        PPOConfig()
        .environment(env=env_name, env_config={})
        .framework("torch")
        .env_runners(num_env_runners=2)
        .training(
            model={"fcnet_hiddens": [64, 64]},
            train_batch_size=4000,
            lr=1e-4
        )
        .resources(num_gpus=0)
    )

    # 4. Build Algorithm
    algo = config.build()

    print(f"Training PPO on {env_name}...")

    rewards = []
    num_iterations = 20

    for i in range(num_iterations):
        result = algo.train()

        # Access reward
        if "env_runners" in result and "episode_reward_mean" in result["env_runners"]:
             mean_reward = result["env_runners"]["episode_reward_mean"]
        elif "episode_reward_mean" in result:
             mean_reward = result["episode_reward_mean"]
        else:
             mean_reward = np.nan

        rewards.append(mean_reward)
        print(f"Iter: {i+1}, Mean Reward: {mean_reward:.2f}")

    # 5. Shutdown
    algo.stop()
    ray.shutdown()

    # 6. Plot Results
    # Handle NaN values for plotting
    plot_rewards = [r if not np.isnan(r) else 0 for r in rewards]

    plt.figure(figsize=(10, 6))
    plt.plot(plot_rewards, label="Mean Reward")
    plt.xlabel("Iteration")
    plt.ylabel("Reward")
    plt.title(f"PPO Training on {env_name}")
    plt.legend()
    plt.grid(True)

    output_file = "ppo_training_plot.png"
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

if __name__ == "__main__":
    train_and_plot()
