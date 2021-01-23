def distance(strand_a, strand_b):
    distancia = 0

    list_strand_a = list(strand_a)

    list_strand_b = list(strand_b)

    if len(list_strand_a) != len(list_strand_b):
        raise ValueError('invalid strand')

    for idx, item_b in enumerate(list_strand_b):
        if item_b != list_strand_a[idx]:
            distancia += 1
    
    return distancia
