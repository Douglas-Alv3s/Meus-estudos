package aula11;

public class Main {
    public static void main(String[] args) {
        Aluno p1 = new Aluno();
        Bolsista p2 = new Bolsista(400);
        // Visitante p3 = new Visitante();


        p1.dadosAluno("Douglas", 19, "M", 211624, "Computação");
        p1.fazerAniversario();
        System.out.println(p1.toString());
        
        p2.dadosAluno("Ana", 54, "F", 124124, "Letras");
        p2.pagarMensalidade();
    }
    
}
