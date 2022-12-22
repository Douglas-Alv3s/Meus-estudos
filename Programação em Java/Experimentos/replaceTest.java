public class replaceTest {
    static private String textoOk;

    static public String codificador(String texto) {
        
        texto = texto.replace("o", "ober");
        texto = texto.replace("a", "ai");

        return texto;
    }

    public static void main(String[] args) {
        String texto = "gato";
        String testada = codificador("gato");
        System.out.println(testada);
        System.out.println("olá");
    }
}
