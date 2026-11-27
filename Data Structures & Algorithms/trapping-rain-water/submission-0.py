class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        lptr, rptr = 0, len(height) - 1
        lmax, rmax = height[lptr], height[rptr]
        water = 0

        while lptr < rptr:
            if lmax <= rmax:
                lptr += 1
                if height[lptr] > lmax:
                    lmax = height[lptr]
                else:
                    water += lmax - height[lptr]
            else:
                rptr -= 1
                if height[rptr] > rmax:
                    rmax = height[rptr]
                else:
                    water += rmax - height[rptr]

        return water
        