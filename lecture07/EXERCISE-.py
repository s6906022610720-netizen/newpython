# Survey results (each list represents a participant's choices)
survey_results = [
    ["Python", "JavaScript", "C++"],         # Participant 1
    ["Python", "JavaScript", "C#"],          # Participant 2
    ["Python", "Java"],                      # Participant 3
    ["Python", "C++", "JavaScript"],         # Participant 4
    ["Python", "JavaScript", "C++", "Java"], # Participant 5
]

# 1. Languages chosen by all participants
choices_sets = [set(p) for p in survey_results]
common_languages = set.intersection(*choices_sets)
print("1. Languages chosen by all participants:", common_languages)

# 2. Languages only chosen by a single participant
from collections import Counter
all_langs = [lang for p in survey_results for lang in p]
counts = Counter(all_langs)
only_one = {lang for lang, c in counts.items() if c == 1}
print("2. Languages only chosen by one participant:", only_one)

# 3. Number of unique languages
unique_languages = set.union(*choices_sets)
print("3. Number of unique languages:", len(unique_languages))

# 4. Languages chosen by exactly two participants
exactly_two = {lang for lang, c in counts.items() if c == 2}
print("4. Languages chosen by exactly two participants:", exactly_two)

# 5. Participants with the same set of languages
same_pairs = []
for i in range(len(choices_sets)):
    for j in range(i + 1, len(choices_sets)):
        if choices_sets[i] == choices_sets[j]:
            same_pairs.append([i + 1, j + 1])
print("5. Participants with the same set of languages:", same_pairs)