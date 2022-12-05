package PROGRAMAÇÂO_OO.aula09;

public class Professor extends Pessoa{
    // Atributos
    private String especialidade;
    private float salario;

    public Professor(String especialidade, float salario) {
        this.especialidade = especialidade;
        this.salario = salario;
    }

    public void receberAum(float aum){
        this.salario += aum;
    }

    public void dadosProfessor(){
        System.out.println("Nome: "+mostarNome());
        System.out.println("Idade: "+mostarIdade());
        System.out.println("Sexo: "+mostarSexo());
        System.out.println("Especialidade: "+this.especialidade);
        System.out.println("Salario: "+this.salario);

    }
    
}
