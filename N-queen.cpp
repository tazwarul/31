#include<bits/stdc++.h>
using namespace std;
int total_solution = 0;
void print(int q_position[], int n)
{
    cout<<"\nsolution"<<++total_solution<<":\n";
    for(int row=0;row<n;row++)
    {
        for(int col=0;col<n;col++)
        {
            if(q_position[row] == col)
            {
                cout<<"Q ";
            }
            else
            {
                cout<<". ";
            }
        }
        cout<<endl;
    }

}
bool is_safe(int q_position[], int c_row, int c_col)
{
    for(int p_row = 0; p_row<c_row; p_row++)
    {
        if(q_position[p_row] == c_col ||
        abs(q_position[p_row] - c_col) == abs(p_row - c_row) )
       {
        return false;
       }

    }
    return true;

}
void place_q(int q_position[], int c_row, int n )
{
    if(c_row == n)
    {
        print(q_position, n);
        return;
    }

    for(int c_col = 0; c_col < n; c_col++)
    {
        if(is_safe(q_position, c_row, c_col))
        {
          q_position[c_row] = c_col;
          place_q(q_position, c_row+1, n);
        }
    }

}
int main()
{
    int n;
    cout<<"Enter the queen: ";

   cin>>n;
   int q_position[n];
   place_q(q_position, 0, n);
   if (total_solution == 0)
   cout << "No solution exists for N = " << n << endl;
    return 0;
}