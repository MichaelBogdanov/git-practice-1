#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define ARR_SIZE 10


void bubble_sort(int *arr)
{
  for(int i = 0; i < ARR_SIZE; i++)
  {
    for(int j = 0; j < ARR_SIZE - 1;j++)
    {
      if(arr[j] > arr[j+1])
      {
        int tmp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tmp;
      }
    }
  }
}

void fill_array(int *arr)
{
  for(int i = 0; i < ARR_SIZE; i++)
  {
    int rand_num = rand() % 100;
    arr[i] = rand_num;
  }
}

void print_arr(int *arr)
{
  for(int i = 0; i < ARR_SIZE; i++)
  {
    printf("%d ", arr[i]);
  }
}

int main()
{
  int arr[ARR_SIZE] = {};
  srand(time(NULL));
  fill_array(arr);
  print_arr(arr);
  printf("\n");
  bubble_sort(arr);
  print_arr(arr);
  return 0;


}
