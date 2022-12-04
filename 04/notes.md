# Notes

- All you need is to compare the bounds of each interval
- Remember that the lower bound needs to be smaller to overlap and the upper bound needs to be larger
- ! In part 1, there is a slight 'irritation', as the containment of the second in first interval is calculated even if the first is already contained in the second. But for the sake of readability, I extracted the bool statements outside the if condition.

## Part 2

- Compare only the upper end of the lower and the lower end of the upper interval, as they are sorted already
