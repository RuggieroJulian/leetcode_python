import bisect
queries =["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
words_freq = sorted([word.count(min(word)) for word in words]) # Do a count of min word in the words array
result = []
for query in queries:
    q_min=min(query) # Get the minimum letter 
    q_count=query.count(q_min) # Count frequency of letter
    # Do a binary search and find the items that have more frequency of min char
    result.append(len(words) - bisect.bisect(words_freq, q_count )) 