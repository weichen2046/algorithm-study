#include <vector>

class Solution
{
public:
  Solution();
  Solution(int maxOps);

  int maxRevenue(std::vector<int> prices);

private:
  void replaceOrInsertTheRevenue(std::vector<int> &revenues, int revenue);

  int mMaxOps;
};