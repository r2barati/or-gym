from gymnasium.envs.registration import register

register(id='NetworkManagement-v0',
	entry_point='or_gym.envs.supply_chain.network_management:NetInvMgmtBacklogEnv'
)

register(id='NetworkManagement-v1',
	entry_point='or_gym.envs.supply_chain.network_management:NetInvMgmtLostSalesEnv'
)
