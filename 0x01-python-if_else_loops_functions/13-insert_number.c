#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: Pointer to the head of the linked list
 * @e_m: Value to be inserted into the new node
 *
 * Return: Pointer to the newly inserted node, or NULL if malloc fails
 */
listint_t *insert_node(listint_t **head, int e_m)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->e_m = e_m;

	if (node == NULL || node->e_m >= e_m)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->e_m < e_m)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
