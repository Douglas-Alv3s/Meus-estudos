public class MeuPrograma {

    private String nome;
    private int idade;
    private Float altura;

    // Construtor 1 - Padrão
    public MeuPrograma(String nome, int idade, Float altura) {
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;

    }

    // Construtor 2 - Com Parâmetros
    // public MeuPrograma()

    public String formatarDados() {
        return "Eu, " + nome + "com altura de "+altura  + " com " + idade + " anos.";

    }

}
