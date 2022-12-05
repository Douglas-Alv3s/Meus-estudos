package aula11;

public class Aluno extends Pessoa {
    private int matricula;
    private String curso;

    
    public void dadosAluno(String nome, int idade, String sexo, int matricula, String curso){
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
        this.matricula = matricula;
        this.curso = curso;
    }
        
    

    public void pagarMensalidade(){
        System.out.println("Mensalidade paga!");
        
    }



    public int getMatricula() {
        return matricula;
    }



    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }



    public String getCurso() {
        return curso;
    }



    public void setCurso(String curso) {
        this.curso = curso;
    }



}
