#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [elem for elem in num_list if elem%2 == 0]
    return new_list

def make_exclamation(sentence_list):
    new_list = [elem +'!' for elem in sentence_list if len(elem) != 0]
    return new_list