public class MathAleatorio {
    public static void main(String[] args){
        
        //Geração de numero de 0.0 a 1.0
        double aleatorio_flot = Math.random();
        System.out.println(aleatorio_flot);
        
        //Aleatorio inteiro
        int aleatorio_inte =(int) (1 + Math.random() * (100 - 1));
        System.out.println(aleatorio_inte); 

    }
    
}
