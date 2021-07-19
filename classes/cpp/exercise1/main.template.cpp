#include <iostream>
#include <sstream>

'STUD.IMPORTS'

'STUD.FUNCTIONS'

int main(int argc, char * argv[])
{
  int a;
  int b;

  std::stringstream ss1(argv[1]);
  ss1 >> a;

  std::stringstream ss2(argv[2]);
  ss2 >> b;

  std::cout << 'STUD.SECRET_NAME'(a,b) << std::endl;
 
  return 0;
}
