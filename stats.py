def number_of_words(booktext):
    numwords = 0
    splittext=booktext.split()
    #print(splittext)
    numwords=len(splittext)
    #print(numwords)
    return numwords


def char_histogram(booktext):
    histogram={}
    counter=0
    for char in booktext:
        lc_char=char.lower()
        old_hist=1
        if lc_char in histogram:
            old_hist=histogram[lc_char]
            histogram[lc_char]=old_hist+1
        else:
            histogram[lc_char]=old_hist
        counter+=1
    #print(len(histogram))
    return histogram

def sorted_hist(histogram):
    temp_hist=list()
    for letter in histogram:
        if letter.isalpha():
            temp_hist.append({"char":letter,"num":histogram[letter]})
    #print(temp_hist)
    temp_hist.sort(reverse=True, key= lambda x:x["num"])
    return temp_hist

def give_num(histdict):
    return histdict["num"]