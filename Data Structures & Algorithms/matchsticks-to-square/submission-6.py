class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)

        # A square is impossible unless the total splits into 4 equal sides
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4

        # No single stick may exceed one side
        if max(matchsticks) > side_length:
            return False

        # Longest first: fails fast, prunes the search tree dramatically
        matchsticks.sort(reverse=True)

        sides = [0] * 4  # current length accumulated on each of the 4 sides

        def place_stick(stick_index: int) -> bool:
            # All sticks placed and no side ever exceeded side_length
            # → every side must equal side_length exactly (sum argument)
            if stick_index == len(matchsticks):
                return True

            current_stick = matchsticks[stick_index]

            for side in range(4):
                if sides[side] + current_stick <= side_length:
                    # choose
                    sides[side] += current_stick

                    # explore
                    if place_stick(stick_index + 1):
                        return True

                    # unchoose (must mirror the choose exactly)
                    sides[side] -= current_stick

                # Symmetry pruning: if this side is empty (either it was
                # empty and the stick didn't fit, or we just undid back to
                # empty), every other empty side is identical — skip them.
                if sides[side] == 0:
                    break

            return False

        return place_stick(0)