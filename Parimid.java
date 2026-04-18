// n=5 , r=1   4sp , 1*
// n=5 , r=2   3sp , 3*
// n=5 , r=3   2sp , 5*
// n=5 , r=4   1sp , 7*
// n=5 , r=5   0sp , 9*

// for spaces the formula will be = (n-r)

// for stars = 2*r-1

class Parimid{
    public static void main(String[] args) {
        int n = 5;
        for (int i = 1; i <= n; i++) {
            for(int j = 1 ; j<=n-i; j++){
            System.out.print("  ");
            }
            for(int j = 1 ; j<=2*i-1; j++){
            System.out.print("* ");
            }
            System.out.println();
            
        }
    }
}