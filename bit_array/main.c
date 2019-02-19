#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>


char* init(int size);
void set(char*p, int i, int value);
char make_zero_mask(int diff);
char make_one_mask(int diff, int value);
int get(char* p, int i);


char* init(int size) {
  int charSize = size / 8 + 1;
  char* p = (char*) malloc(charSize * sizeof(char));
  return p;
}


void set(char*p, int i, int value) {
  assert(value == 0 || value == 1);
  int part_index = i / 8;
  int diff = i % 8;
  char block = p[part_index];
  char zero_mask = make_zero_mask(diff);
  block = block & zero_mask;
  char one_mask = make_one_mask(diff, value);
  block = block | one_mask;
  p[part_index] = block;
}


int get(char* p, int i) {
  int part_index = i / 8;
  int diff = i % 8;
  char item = p[part_index];
  for (int j = 0; j < diff; j++) {
    item = item >> 1;
  }
  return item & 1;
}


char make_zero_mask(int diff) {
  char c = -1;
  int i = pow(2, diff);
  return c - i;
}


char make_one_mask(int diff, int value) {
  int i = pow(2, diff);
  return value * i;
}


int main(int argc, char** argv) {
  char* p = init(100);
  printf("%p\n", p);
  set(p, 88, 1);
  printf("%d\n", get(p, 89));
  printf("%d\n", get(p, 88));
}
