#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zombie;

	while (i <= 5)
	{
		zombie = fork();
		if (zombie == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", zombie);
		i++;
	}
	infinite_while();
	return (0);
}
