def count_names_cut(ranks):
    cut_count = 1
    min_rank = float('inf')  # Initialize min_rank as positive infinity
    
    for rank in ranks:
        if rank < min_rank:
            min_rank = rank
        else:
            cut_count += 1
    
    return cut_count

n=int(input())
a=input()
rank_list = [int(i) for i in a.split()]

cut_names = count_names_cut(rank_list)
print(cut_names)
    