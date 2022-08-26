scientific_research = [int(input()) for _ in range(int(input()))]

# del scientific_research[scientific_research.index(max(scientific_research))]
# del scientific_research[scientific_research.index(min(scientific_research))]

scientific_research.remove(max(scientific_research))
scientific_research.remove(min(scientific_research))

print(*scientific_research, sep='\n')