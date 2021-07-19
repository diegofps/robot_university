'STUD.IMPORTS'

'STUD.FUNCTIONS'

int main(int argc, char * argv[])
{
  int a;
  int b;

  sscanf(argv[1], "%d", &a);
  sscanf(argv[2], "%d", &b);

  printf("%d", 'STUD.SECRET_NAME'(a, b));

  return 0;
}
