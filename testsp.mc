struct Point {
  int x;
  int y;
};

int main() {
  struct Point p1;
  p1.x = 5;
  p1.y = 10;

  struct Point *p2 = &p1;
  printf("%d\n", p2->x);
}
