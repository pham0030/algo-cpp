#include <iostream>

#include <string>

 

using namespace std;

 

int

edit_distance (const string & str1, const string & str2)

{

  int n = str1.size ();

  int m = str2.size ();

  int D[n + 1][m + 1];

  int i = 0;

 

  while (i <= n)

    {

      D[i][0] = i;

      i++;

    }

 

  i = 1;

  while (i <= m)

    {

      D[0][i] = i;

      i++;

    }

 

  for (int i = 1; i <= n; i++)

    {

      for (int j = 1; j <= m; j++)

                {

                  int insertion = D[i][j - 1] + 1;

                  int deletion = D[i - 1][j] + 1;

                  int match = D[i - 1][j - 1];

                  int mismatch = D[i - 1][j - 1] + 1;

                  if (str1[i - 1] == str2[j - 1])

                    {

                      D[i][j] = min (insertion, min (deletion, match));

                    }

                  else

                    {

                      D[i][j] = min (insertion, min (deletion, mismatch));

                    }

 

                }

    }

 

  return D[n][m];

}

 

int

main ()

{

  string str1;

  string str2;

  cin >> str1 >> str2;

  cout << edit_distance (str1, str2) << endl;

  return 0;

}