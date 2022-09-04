/*#include <iostream>

using namespace std;
int Fun(int n)
{
    if (n == 1 || n == 0)
    {
        return n;
    }
    else
    {
        return Fun(n - 1) + Fun(n - 2);
    }
}
int main()
{
    int n, i = 0;
    for (int i = 0; i < 20; i++)
    {
        cout << " " << Fun(i);
    }
    return 0;
}*/
// dp-topdown =recursion +memoization
#include <iostream>
#include <vector>
using namespace std;
int Fun(int n, vector<int> &dp)
{
    if (n <= 1)
    {
        return n;
    }
    if (dp[n] != -1)
    {
        return dp[n];
    }
    dp[n] = Fun(n - 1, dp) + Fun(n - 2, dp);
    return dp[n];
}
int main()
{
    int n, i = 0;
    n = 9;
    vector<int> dp(n + 1);
    for (int i = 0; i <= n; i++)
    {
        dp[i] = -1;
    }
    cout << Fun(n, dp) << endl;
    return 0;
}
// time O(N) space O(N) +O(N)
// dp bottomup tabulation
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    cout << "dd";
    int n = 9;
    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n + 1; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[n] << endl;
}
// time O(N) space O(N)
// further modification to tabulation by removing dp array
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n = 9;
    int prev1 = 0;
    int prev2 = 1;
    for (int i = 2; i <= n; i++)
    {
        int current = prev1 + prev2;
        prev1 = prev2;
        prev2 = current;
    }
    std::cout << prev2 << std::endl;
}
// time O(N) space O(1)