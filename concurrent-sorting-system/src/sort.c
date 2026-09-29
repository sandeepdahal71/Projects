#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
typedef struct{int*a;int l,r;}Job; void insertion(int*a,int l,int r){for(int i=l+1;i<r;i++){int x=a[i],j=i-1;while(j>=l&&a[j]>x){a[j+1]=a[j];j--;}a[j+1]=x;}}
void*worker(void*p){Job*j=p;insertion(j->a,j->l,j->r);return NULL;} void merge(int*a,int m,int n){int*t=malloc(n*sizeof(int)),i=0,j=m,k=0;while(i<m&&j<n)t[k++]=a[i]<a[j]?a[i++]:a[j++];while(i<m)t[k++]=a[i++];while(j<n)t[k++]=a[j++];for(i=0;i<n;i++)a[i]=t[i];free(t);}
int main(int ac,char**av){int n=ac>1?atoi(av[1]):10000;int*a=malloc(n*sizeof(int));srand(42);for(int i=0;i<n;i++)a[i]=rand();Job x={a,0,n/2},y={a,n/2,n};pthread_t p,q;clock_t s=clock();pthread_create(&p,0,worker,&x);pthread_create(&q,0,worker,&y);pthread_join(p,0);pthread_join(q,0);merge(a,n/2,n);printf("sorted %d integers in %.3fs\n",n,(double)(clock()-s)/CLOCKS_PER_SEC);free(a);}
