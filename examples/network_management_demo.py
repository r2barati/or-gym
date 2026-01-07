
import or_gym
import matplotlib.pyplot as plt
import numpy as np

# Create the environment
env = or_gym.make('NetworkManagement-v1')

# Reset the environment
state, info = env.reset()

# Run a random agent for a few steps
done = False
steps = 0
while not done and steps < 100:
    action = env.action_space.sample()
    state, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    steps += 1
    print(f"Step: {steps}, Reward: {reward}")

# Plot the network
# Note: plot_network might block execution until window is closed if not handled
# We just call it to show it exists and works (it uses matplotlib)
try:
    if hasattr(env, "plot_network"):
        env.plot_network()
    elif hasattr(env.unwrapped, "plot_network"):
        env.unwrapped.plot_network()
    else:
        print("plot_network not found on environment.")
except Exception as e:
    print(f"Plotting failed (expected in headless env if no display): {e}")

print("Done.")
