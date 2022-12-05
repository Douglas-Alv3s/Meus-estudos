public class Metodos {
    

    // Void --> não tem retorno
    // tip --> tem retorno

    // -----VOID-------------------------
    /* 
    static void soma(int a, int b){
        int s = a+b;
        System.out.println("O Resultado da soma é "+s);
    } 
    */
    static int soma(int a, int b){
        int s = a+b;
        return s;
    }


    public static void main(String[] args){
        int sm = soma(9,4);
        System.out.println("A soma é "+sm);
    }
}
