// *
// **
// ***
// ****
// *****

public class patterns{
    public static void main(String[] args) {
        // int n = 5;
        // for (int i = 0; i<=n; i++){
        //     for (int j = 0; j<i; j++){
        //         System.out.print("* ");
        //     }
        //     System.out.println();
        // }


    // for rhombus
        int n = 5;

        for(int i = 1 ; i<=n; i++){
            //spaces
            for(int j = 1; j<=n-i; j++){
                System.out.print(" ");
            }
            //stars
            for(int j = 1; j<=n; j++){
                System.out.print("* ");

            }
            System.out.println();
        }
        
    }
}