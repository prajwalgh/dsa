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
