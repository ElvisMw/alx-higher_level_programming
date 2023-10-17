#include "lists.h"
/**
 * check_cycle - Checks whether the given
 * singly linked list has a cycle
 * @list: Represents pointer to the list's head.
 * Return: absence of cyle returns 0
 * presence of cycle returns 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}

