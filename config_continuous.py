import pickle

config_dict = {
    "observation": {
        "type": "Kinematics",
        "vehicles_count": 8,
        "features": [
            "presence",
            "x",
            "y",
            "vx",
            "vy",
            "cos_h",
            "sin_h",
            "relative_heading",
        ],
        "features_range": {
            "x": [-100, 100],
            "y": [-100, 100],
            "vx": [-30, 30],
            "vy": [-30, 30],
        },
        "absolute": True,
        "normalize": True,
    },
    "action": {
        "type": "ContinuousAction",
        "longitudinal": True,  # Contrôle d'accélération
        "lateral": True,  # Contrôle de direction
    },
    "lanes_count": 3,
    "vehicles_count": 10,
    "duration": 80,  # [s]
    "initial_spacing": 2,
    "collision_reward": -2,
    "right_lane_reward": 0.1,
    "high_speed_reward": 0.4,
    "lane_change_reward": -0.05,
    "reward_speed_range": [
        15,
        25,
    ],
    "simulation_frequency": 10,  # [Hz]
    "policy_frequency": 2,  # [Hz]
    "other_vehicles_type": "highway_env.vehicle.behavior.IDMVehicle",
    "screen_width": 800,  # [px]
    "screen_height": 200,  # [px]
    "centering_position": [0.4, 0.5],
    "scaling": 7.0,
    "show_trajectories": True,
    "render_agent": True,
    "offscreen_rendering": False,
    "disable_collision_checks": False,
}

with open("continuous_config.pkl", "wb") as f:
    pickle.dump(config_dict, f)

# Pour utiliser cette configuration:
# env = gym.make("highway-v0", render_mode="rgb_array")
# env.unwrapped.configure(config_dict)
# print(env.reset())
