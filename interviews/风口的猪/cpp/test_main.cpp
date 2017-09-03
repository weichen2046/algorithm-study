
#include <cassert>
#include <iostream>

#include "Solution.h"

using namespace std;

void test_case1()
{
    int pricesArray[] = {3, 8, 5, 1, 7, 8};
    std::vector<int> prices(pricesArray, pricesArray + sizeof(pricesArray) / sizeof(int));
    int revenue = Solution(2).maxRevenue(prices);
    assert(12 == revenue);
}

void test_case2()
{
    int pricesArray[] = {3, 8, 5, 1, 7, 8, 9, 2, 21, 5, 6, 7};
    std::vector<int> prices(pricesArray, pricesArray + sizeof(pricesArray) / sizeof(int));
    int revenue = Solution(2).maxRevenue(prices);
    assert(27 == revenue);
}

void test_case3()
{
    int pricesArray[] = {3, 8, 5, 1, 7, 8, 9, 2, 21, 5, 6, 7};
    std::vector<int> prices(pricesArray, pricesArray + sizeof(pricesArray) / sizeof(int));
    int revenue = Solution(3).maxRevenue(prices);
    assert(32 == revenue);
}

void test_case4()
{
	int pricesArray[] = {1, 1, 1, 1};
    std::vector<int> prices (pricesArray, pricesArray + sizeof(pricesArray) / sizeof(int));
    int revenue = Solution(2).maxRevenue(prices);
    cout<<revenue<<endl;
    assert (0 == revenue);
}

int main(int argc, char **argv)
{
    test_case1();
    test_case2();
    test_case3();
    test_case4();
    return 0;
}