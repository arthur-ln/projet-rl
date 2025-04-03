import pickle

config_dict = {
    "observation": {
        "type": "TimeToCollision",
        "vehicles_count": 12,
        "features": ["presence", "x", "y", "vx", "vy", "ttc", "heading"],
        "features_range": {
            "x": [-100, 100],
            "y": [-100, 100],
            "vx": [-25, 25],
            "vy": [-25, 25],
            "ttc": [0, 10],
        },
        "grid_size": [[-25, 25], [-25, 25]],
        "grid_step": [5, 5],
        "absolute": False,
    },
    "action": {
        "type": "DiscreteMetaAction",
    },
    "lanes_count": 5,
    "vehicles_count": 15,
    "duration": 50,  # [s]
    "initial_spacing": 1,
    "collision_reward": -1.5,
    "right_lane_reward": 0.2,
    "high_speed_reward": 0.3,
    "lane_change_reward": -0.1,
    "reward_speed_range": [
        18,
        28,
    ],
    "simulation_frequency": 8,  # [Hz]
    "policy_frequency": 2,  # [Hz]
    "other_vehicles_type": "highway_env.vehicle.behavior.IDMVehicle",
    "screen_width": 700,  # [px]
    "screen_height": 180,  # [px]
    "centering_position": [0.35, 0.5],
    "scaling": 6.0,
    "show_trajectories": True,
    "render_agent": True,
    "offscreen_rendering": False,
    "disable_collision_checks": False,
}

with open("stablebaselines_config.pkl", "wb") as f:
    pickle.dump(config_dict, f)

# Pour utiliser cette configuration avec StableBaselines:
# import gym
# import highway_env
# from stable_baselines3 import PPO
#
# env = gym.make("highway-v0", render_mode="rgb_array")
# env.unwrapped.configure(config_dict)
# model = PPO("MlpPolicy", env, verbose=1)
# model.learn(total_timesteps=10000)
