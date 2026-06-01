class Solution:
    # WRONG ASSUMPTION:
    #   I thought the walls in between column i and the edges mattered.
    #   They don't — only the TALLEST wall on each side matters. Shorter
    #   walls in between just let water flow over them until it hits the
    #   real cap.
    #
    # KEY INSIGHT:
    #   Water above column i is capped by the shorter of its two tallest walls:
    #       water[i] = min(leftMax[i], rightMax[i]) - height[i]
    #   Why min? Water spills over the SHORTER wall first — that's the real
    #   ceiling.
    #
    # APPROACH:
    #   Two pointers from both ends. Track leftMax and rightMax as we go.
    #   At each step, move the pointer on the side with the smaller max —
    #   that side's water level is already locked in, because the other side
    #   has something at least as tall further out.
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        result = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]

        return result