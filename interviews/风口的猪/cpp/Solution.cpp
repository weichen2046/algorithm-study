#include "Solution.h"

Solution::Solution() : mMaxOps(2)
{
}

Solution::Solution(int maxOps) : mMaxOps(maxOps)
{
}

int Solution::maxRevenue(std::vector<int> prices)
{
    std::vector<int> maxRevens;

    // sum of continues positive delta
    int sum = 0;
    for (std::vector<int>::iterator it = (prices.begin() + 1); it != prices.end(); ++it)
    {
        int delta = *it - *std::prev(it);
        if (delta > 0)
        {
            sum += delta;
        }
        else
        {
            if (sum > 0)
            {
                replaceOrInsertTheRevenue(maxRevens, sum);
            }
            // reset sum
            sum = 0;
        }
    }
    replaceOrInsertTheRevenue(maxRevens, sum);

    int res = 0;
    for (auto &n : maxRevens)
    {
        res += n;
    }
    return res;
}

void Solution::replaceOrInsertTheRevenue(std::vector<int> &revenues, int revenue)
{
    if (revenues.size() < mMaxOps)
    {
        // insert by descending order
        std::vector<int>::iterator it = revenues.begin();
        for (; it != revenues.end(); ++it)
        {
            if (*it <= revenue)
            {
                break;
            }
        }
        revenues.insert(it, revenue);
        return;
    }

    // replace the smallest revenue
    std::vector<int>::reverse_iterator it = revenues.rbegin();
    if (*it < revenue)
    {
        *it = revenue;
    }
}
