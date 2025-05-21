#ex1
struct Person {
    int age;
    char grade;
};

int main() {
    struct Person p;
    p.age = 20;
    p.grade = 'A';
    printf("%d %c", p.age, p.grade);
    return 0;
}
#ex2
int main() {
    int x = 5;
    int y = 10;
    int total = x + y;
    printf("%d", total);
    return 0;
}