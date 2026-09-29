#include <math.h>
#include <stdlib.h>
typedef struct{int u,v;double w;}Edge;static int cmp(const void*a,const void*b){double x=((Edge*)a)->w,y=((Edge*)b)->w;return(x>y)-(x<y);}static int find(int*p,int x){return p[x]==x?x:(p[x]=find(p,p[x]));}double kruskal(Edge*e,int m,int n){qsort(e,m,sizeof(*e),cmp);int*p=malloc(n*sizeof(int));for(int i=0;i<n;i++)p[i]=i;double total=0;int used=0;for(int i=0;i<m&&used<n-1;i++){int a=find(p,e[i].u),b=find(p,e[i].v);if(a!=b){p[a]=b;total+=e[i].w;used++;}}free(p);return total;}
