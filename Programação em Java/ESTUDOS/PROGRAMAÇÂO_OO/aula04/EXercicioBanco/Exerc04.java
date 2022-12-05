package PROGRAMAÇÂO_OO.aula04.EXercicioBanco;

public class Exerc04 {
    public static void main(String[] args) {
        ContaBanco p1 = new ContaBanco();
        p1.abrirConta(123456, "cc","joão");

        p1.depositar(100);
        p1.sacar(150);

        p1.estadoAtual();
    }
    
}
