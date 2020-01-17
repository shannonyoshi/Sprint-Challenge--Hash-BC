#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    i=0
    while i< length:
        print("while inserting")
        hash_table_insert(ht, weights[i], i)
        i+=1
    i=0
    while i<length:
        print(f"limit-weights[i]: {limit} - {weights[i]}")
        wanted_value = limit-weights[i]
        print(f"while wanted value: {wanted_value}")
        index = hash_table_retrieve(ht, wanted_value)
        if index is not None:
            print(f"index(is true): {index}, i: {i}")
            answer = [i,index]
            print(f"answers before sort: {answer}")
            answer.sort(reverse=True)
            print(f"answers after sort: {answer}")
            return answer
        i+=1

    return None


def print_answer(answer):
    print("in print_answer: ", answer)
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")
