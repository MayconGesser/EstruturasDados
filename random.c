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

char convAsciiMaiuscula(char c)	//essa funcao pega o codigo ascii associado a cada char,
{								//e subtrai 32, pois eh possivel obter qualquer letra maiuscula
	if(c == ' ')				//subtraindo 32 do codigo ascii da minuscula (vide tabela ascii)
	{							//ela em seguida converte novamente o codigo ascii em um caractere
		return ' ';				//e testa para saber se eh um valor aceitavel para ser retornado
	}

	char asciiMaiuscula;
	char retornosAceitaveis[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
	'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', '\0'};
	int tamanho = getlength(retornosAceitaveis);
	int ascii = getascii(c);
	ascii = ascii - 32;
	asciiMaiuscula = (char) ascii;
	bool ehRetornoAceitavel = false;

	for(int i = 0; i<tamanho; i++)
	{
		if(retornosAceitaveis[i] == asciiMaiuscula)
		{
			ehRetornoAceitavel = true;
		}
	}

	char retorno = ehRetornoAceitavel ? asciiMaiuscula : '.';
	return retorno;
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