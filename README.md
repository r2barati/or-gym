# OR-Gym: Supply Chain Environments

This repository contains the `NetworkManagement` environments from OR-Gym, a set of environments for developing reinforcement learning agents for operations research problems.

## Installation

### Prerequisites
- Python 3.7+
- pip

### Install from source
```bash
pip install -e .
```

### Install dependencies for training examples
To run the included examples with Ray/RLlib:
```bash
pip install "ray[rllib]" torch gymnasium typer
```

## Usage

### Basic Usage
```python
import or_gym

# Create the environment
env = or_gym.make('NetworkManagement-v1')

# Reset
state, info = env.reset()

# Step
action = env.action_space.sample()
next_state, reward, terminated, truncated, info = env.step(action)
```

### Training an Agent (PPO with RLlib)

An example script is provided in `examples/train_network_main.py` which demonstrates how to train a PPO agent using Ray RLlib on the `NetworkManagement-v1` environment.

To run the training:
```bash
python examples/train_network_main.py
```
This script will:
1. Initialize Ray.
2. Train a PPO agent for a few iterations.
3. Save a plot of the training rewards to `ppo_training_plot.png`.

## Environments

The following environments are available:
- `NetworkManagement-v0`: Backlog variant.
- `NetworkManagement-v1`: Lost sales variant.

## License
MIT
