class Solution
{
  public:
    vector<string> findWords(vector<string> &words)
    {
        vector<string> preDefineds;
        preDefineds.push_back("qwertyuiop");
        preDefineds.push_back("asdfghjkl");
        preDefineds.push_back("zxcvbnm");

        vector<string>::iterator it = words.begin();
        while (it != words.end())
        {
            string word = *it;
            int breakCount = 0;
            for (vector<string>::iterator pIt = preDefineds.begin(); pIt != preDefineds.end(); pIt++)
            {
                string pS = *pIt;
                string::iterator cIt = word.begin();
                for (; cIt != word.end(); cIt++)
                {
                    char c = *cIt;
                    // to lower case
                    if (c <= 'Z' && c >= 'A')
                    {
                        c = c - ('Z' - 'z');
                    }
                    if (string::npos == pS.find(c))
                    {
                        breakCount++;
                        break;
                    }
                }
                if (cIt == word.end())
                {
                    break;
                }
            }
            if (breakCount >= 3)
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