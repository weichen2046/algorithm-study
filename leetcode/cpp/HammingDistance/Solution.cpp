class Solution {
public:
    int hammingDistance(int x, int y) {
        int dist = 0;
        int xorValue = x ^ y;
        for (int i=0; i<32; i++) {
            if ((xorValue >> i) & 1 == 1) {
                dist++;
            }
        }
        return dist;
    }
};