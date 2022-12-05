package aula11;


abstract class Pessoa {
    protected String nome;
    protected int idade;
    protected String sexo;

    public void dadosImplement(String name, int idade, String sexo){
        this.nome = name;
        this.idade = idade;
        this.sexo = sexo;
    }

    public void fazerAniversario(){
        System.out.println("Parabéns pelo seu Aniversario "+this.nome);
        this.idade++;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getSexo() {
        return sexo;
    }

    @Override
    public String toString() {
        return "Pessoa [nome=" + nome + ", idade=" + idade + ", sexo=" + sexo + "]";
    }
}
