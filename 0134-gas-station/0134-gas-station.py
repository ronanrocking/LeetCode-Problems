class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0

        tank = 0
        start = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]

            total_gas += gas[i]
            total_cost += cost[i]
            tank += difference

            if tank < 0:
                start = i + 1
                tank = 0

        if total_gas < total_cost:
            return -1

        return start