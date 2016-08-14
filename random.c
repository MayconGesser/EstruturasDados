#include <stdio.h>
#include <stdbool.h>


int getlength(char* arr)	//essa funcao determina o tamanho de um array baseado nas iteracoes
{							//q ela executa ateh chegar no caractere q determina o fim do array
 							//(quando o array eh de chars, pra int nao funfa)
	int i = 0;				//q eh o '\0'. Em C, nao ha como pegar o comprimento de um array diretamente
	while(arr[i] != '\0')	//nao tem como fazer array.length como em java, entao tem q improvisar...
	{
		i++;
	}
	return i;
}

int getascii(char c)		//essa funcao retorna o codigo ascii associado a um char
{
	int ascii;
	char b;
	b = c;
	ascii = (int)b;
	return ascii;
}

char convAsciiMaiuscula(char c)	//essa funcao testa o caractere de argumento para saber se eh um caractere minusculo
{								//se nao for, retorna o proprio caractere de argumento, pois essa funcao soh
								//almeja modificar caracteres minusculos

	char entradas_aceitaveis[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
									'p','q','r','s','t','u','v','x','y','w','z','\0'};

	int iteracoes = getlength(entradas_aceitaveis);
	bool eh_aceitavel = false;

	for(int i = 0; i<iteracoes; i++)
	{
		if(c == entradas_aceitaveis[i])
		{
			eh_aceitavel = true;
		}
	}

	char retorno;
	retorno = eh_aceitavel ? (char)(getascii(c)-32) : c;		
	return retorno;


	//essa eh uma verificacao com operador ternario
	//se o argumento de entrada for aceitavel, a funcao subtrai 32 do codigo ascii associado ao caractere
	//na tabela ascii, eh possivel obter a letra maiuscula de uma minuscula subtraindo 32 de seu codigo
	//o operador ternario faz o cast de volta para para char a partir dessa subtracao															
}

int converterMaiusculas(char* arr)	//essa funcao basicamente aceita uma string como entrada e aplica a funcao
{									//acima a cada um de seus caracteres
    int elementos = getlength(arr);
    for(int i = 0; i<elementos; i++)
    {
        int maiuscula = convAsciiMaiuscula(arr[i]);
        arr[i] = (char)maiuscula;
    }
    return 0;
}

int imprimeArrayChar(char* array)	//funcao de impressao de string
{
    int nelementos = getlength(array);
	for(int i = 0; i<nelementos; i++)
	{
		printf("%c ", array[i]);
	}

	printf("\n");

	return 0;
}

int main()
{
	int tam = 100;						//o tamanho do buffer da string estah hard-coded aki, oq nao deveria ser o caso
    printf("\nDigite uma frase\n");		//ha jeitos mais elegantes de se fazer, mas serve para ter uma ideia
    char string[tam];					
    scanf("%[^\n]", string);
    converterMaiusculas(string);
 	imprimeArrayChar(string);
    return 0;
}
