## Tipos de Saídas

[float] nota = `8.5`

>> Saida de dados simples
[System.out.print]("Sua nota é" + `nota`); --> `Saida padrão`

[System.out.print`ln`]("Sua nota é" + `nota`) --> `Saida com quebra de linha`

>> Saida de dados paramétricas
[System.out.print`f`]("Sua nota é [%.2f]", `nota`)

[System.out.´format´]("Sua nota é [%.2f]", `nota`)


## Entrada de Dados

>>import
[import] `java.util.Scanner`;

>>Class importada
[Scanner] teclado = `new` [Scanner](System.in);

>>Repassando os parametros para os tipos primitivos
[int] idade = `teclado.nextInt();` --> Tipo Inteiro
[float] salario = `teclado.nextFloat();` --> Tipo Float
[String] nome = `teclado.nextLine():` --> Tipo String



## Convertendo Números Inteiros para String

>> Tipos inteiros tem incompatibilidade com Strings, para resolver esse problema
>> de incompatibilidade é necessário fazer através de [Classes_invólucro]

> Converte um numero inteiro para uma String <
[String] valor = [Integer]`.toString(idade);`

> Converte uma String para um numero inteiro <
[int] idade = [Integer]`.parseInt(valor);`

> Converter uma String para um numero Float <
[float] valor = [Float]`.parseFloat(valor);`



