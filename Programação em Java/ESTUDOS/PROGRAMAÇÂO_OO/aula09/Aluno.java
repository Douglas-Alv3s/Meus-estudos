package PROGRAMAÇÂO_OO.aula09;

public class Aluno extends Pessoa{
    private boolean matr;
    private String curso;

    
    public Aluno(String curso) {
        this.matr = true;
        this.curso = curso;
    }


    public void cancelarMatr(){
        if (this.matr == true){
            this.matr = false;
            System.out.println("Desmatricula realizada");
        }else{
            this.matr = false;
            System.out.println("Ja está desmatriculado");
        }
    }

    public void dadosAluno(){
        System.out.println("Nome: "+mostarNome());
        System.out.println("Idade: "+mostarIdade());
        System.out.println("Sexo: "+mostarSexo());
        System.out.println("Matriculado: "+this.matr);
        System.out.println("Curso: "+this.curso);

    }
    
}
