public class Question_01{

    public static void main(String[] args) {
        System.out.println("Hello World");
    }

    // define three sum functions
    public static int sum(int[] a){
        for(int i = 0; i < a.length; i++){
            for(int j = 0; j < a.length; j++){
                for(int k = 0; k < a.length; k++){
                    if(a[i]!=a[j] && a[j]!=a[k] && a[k]!=a[i] && a[i]+a[j]+a[k]==0){
                        return a[i]+a[j]+a[k];
                    }
                }
            }
        }
        return 0;
    }
    
}