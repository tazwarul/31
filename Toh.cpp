#include <bits\stdc++.h>
using namespace std;

void Toh(int n, char src, char aux, char dest)
{
    if (n == 1)
    {
        cout << "Move disk- " << n << " from " << src << " To " << dest << endl;
        return;
    }

    Toh(n - 1, src, dest, aux);
    cout << "Move disk - " << n << " from " << src << " To " << dest << endl;
    Toh(n - 1, aux, src, dest);
}

int main()
{
    int n;
    cin >> n;
    Toh(n, 'A', 'B', 'C');
    cout << " Total Moves :" << pow(2, n) - 1;
    return 0;
}
