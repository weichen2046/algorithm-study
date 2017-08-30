class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (string::iterator it = moves.begin(); it != moves.end(); it++) {
            char m = *it;
            switch (m) {
            case 'U': y++; break;
            case 'D': y--; break;
            case 'R': x++; break;
            case 'L': x--; break;
            }
        }
        return x == 0 && y == 0;
    }
};