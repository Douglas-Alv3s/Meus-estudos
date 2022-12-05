package PROGRAMAÇÂO_OO.aula08;

public class Main {
    public static void main(String[] args) {
        Pessoas leitor = new Pessoas("Douglas", 15, "masculino");
        leitor.dadosPessoa();

        Livro libre = new Livro("Five Ninghts", "Scott Calton", 365, 1, leitor);
        System.out.println(libre.detalhes());
        libre.abrir();
        // libre.fechar();
        libre.avançaPag();
        // libre.folhear();
    }
}
