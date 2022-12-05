package PROGRAMAÇÂO_OO.aula09;

public class Main {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        Funcionario p2 = new Funcionario("Repositor");    
        Aluno p3 = new Aluno("Computação");
        Professor p4 = new Professor("Matematica", 1200.1f);

        p1.dados("Douglas Alves", 19, "masculino");
        p2.dados("Mario", 26, "masculino");
        p3.dados("Aline",16, "feminino");
        p4.dados("Jucielly", 19, "feminino");

        p4.dadosProfessor();
    }
    
}
