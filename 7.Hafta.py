class my_class():
    def __init__(self,my_file=""):
        f= open("...\\file.txt", "r")
        my_content = f.read()
        my_sentences = my_content.split(".")#cumleler my_sentences listesine atandı
        self.my_words = []
        for sentence in my_sentences:
            words_in_the_sentence = sentence.split(" ")
            for word_1 in words_in_the_sentence:
                self.my_words.append(word_1)
                
                
        self.my_frequency_1()
        self.my_frequency_2()
        self.write_frequency_1()
        self.write_frequency_2()
        
    def my_frequency_1(self):
        self.frequency_list_1 = {}
        for word in self.my_words:
            if(word in self.frequency_list_1):
                self.frequency_list_1[word] += 1
            else:
                self.frequency_list_1[word] = 1
    def write_frequency_1(self):
        for word_1 in self.frequency_list_1:
            print(word_1+" "+ str(self.frequency_list_1[word_1]))
    def my_frequency_2(self):
        self.frequency_list_2 = {}
        for i in range(len(self.my_words)-1):
            w_1, w_2 = self.my_words[i], self.my_words[i+1]
            
            if((w_1,w_2) in self.frequency_list_2):
                self.frequency_list_2[(w_1,w_2)] += 1
            else:
                self.frequency_list_2[(w_1,w_2)] = 1
                
    def write_frequency_2(self):
        for word_1 in self.frequency_list_2:
            print(str(word_1)+" "+ str(self.frequency_list_2[word_1]))
    
    
my_class_1 = my_class()
#print(my_class_1.my_words,end="\n")
print(len(my_class_1.my_words))
print(my_class_1.my_words[1])
print("Aradigin kelimeden su kadar var --->",my_class_1.frequency_list_1['all'])
