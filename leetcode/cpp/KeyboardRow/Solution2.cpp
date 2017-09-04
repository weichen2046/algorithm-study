class Solution
{
  public:
    vector<string> findWords(vector<string> &words)
    {
        int preDefRows[] = {2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3};
        for (vector<string>::iterator it = words.begin(); it != words.end();)
        {
            string word = *it;
            bool searching = false;
            int wRow = 0;
            int keep = true;
            for (string::iterator cIt = word.begin(); cIt != word.end(); cIt++)
            {
                char c = *cIt;
                if (c <= 'Z' && c >= 'A')
                {
                    c -= 'Z' - 'z';
                }
                int cRow = preDefRows[c - 'a'];
                if (searching && wRow != cRow)
                {
                    keep = false;
                    break;
                }
                wRow = cRow;
                searching = true;
            }
            if (!keep)
            {
                words.erase(it);
            }
            else
            {
                it++;
            }
        }
        return words;
    }
};