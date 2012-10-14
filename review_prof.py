import pstats
p = pstats.Stats('profile.out')
p.strip_dirs().sort_stats('percall', 'cum').print_stats()