#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def __str__(self):
        return f"Source: {self.source}, Destination: {self.destination}"


def reconstruct_trip(tickets, length):
    # for ticket in tickets:
    #     print("ticket: ", ticket)
    hashtable = HashTable(length)
    route = [None]*length
    first_ticket=None
    i=0
    while i< length:
        if tickets[i].source == "NONE":
            first_ticket = tickets[i]
            #print("first_ticket: ", first_ticket)
        else:
            #print(tickets[i].source)
            hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        i+=1

    #print("first_ticket2: ", first_ticket)
    destination = first_ticket.destination
    route[0]=destination
    i=1
    while i< length:
        #print("ROUTE: ", route)
        next_destination = hash_table_retrieve(hashtable, destination)
        #print("next_desination", next_destination)
        route[i]=next_destination
        destination = next_destination
        i+=1
    #print(route)
    return route
