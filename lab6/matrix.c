double C[N][N];
double A[N][N], B[N][N];
double wall_clock();
int main(int argc, char** argv[]){
	int i, j, k;
	double t0, t1;
	for (i=0; i < N ; i++) {
		for (j=0; j < N; j++) {
			C[i][j] = 0; B[i][j] = (double)i*j; A[i][j]=(double)i*j;
		}
	}
	t0 = wall_clock(); /* finding the best i-j-k order */
	for (#ii=0; #ii < N; #ii++)  
		for (#jj=0; #jj < N; #jj++)
			for (#kk=0; #kk < N; #kk++) 
				C[i][j] += A[i][k]*B[k][j];
	t1 = wall_clock() - t0;
}

#include <sys/time.h>
#include <sys/resource.h>
double wall_clock(){
	struct timeval tp;
	struct timezone tzp;double t;

	gettimeofday(&tp, &tzp);
	t = (tzp.tz_minuteswest*60 + tp.tv_sec)*1.0e6 
		+ (tp.tv_usec)*1.0;
	return t;
}