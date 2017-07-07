#include <stdio.h>
#include <stdlib.h>

#define N 10

int divide(int a[],int low , int high);
void sort(int a[],int low,int high);

int main(int argc, char *argv[])
{

	int a[N] = { 3,5,7,12,15,1,17,2,1,6 },i;

	sort(a, 0, N-1);
	for (int i = 0; i < N-1; i++)
	{
		printf("%d ", a[i]);
	}
	

	system("PAUSE");
	return 0;
}
void sort(int a[], int low, int high)
{
	int mid;
	if (low >= high) return;
	mid = divide(a, low, high);
	if (low >= high) return;
	sort(a, low, mid - 1);
	if (low >= high) return;
	sort(a,mid + 1,high);
}
int divide(int a[], int low, int high)
{
	int center;
	center = a[low];

	while (1) {
		while (low < high&&center <= a[high]) high--;
		if (low >= high) break;
		a[low++] = a[high];
		if (low >= high) break;
		while (low < high&&center >= a[low]) low++;
		if (low >= high) break;
		a[high--] = a[low];
		if (low >= high) break;

	}
	a[low] = center;
	return low;

}
