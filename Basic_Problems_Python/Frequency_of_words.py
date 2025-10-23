def frequency(word):
    lst=word.split()
    freq=dict()
    for word in lst:
        freq[word]=freq.get(word,0)+1

    # for key in freq.items():
    #     print(key)
    
    for key in freq.keys():
        print(f"{key} --> {freq.get(key)}")   

frequency(input("Enter the sentence : "))