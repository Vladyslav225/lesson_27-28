# Вывод чисел > 6
def create_new_list(list_):
     new_list = []

     for n in list_:
          if n > 6:
               new_list.append(n)

create_new_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

new_list = [number for number in list_ if number > 6]
print(new_list)



# Поиск дублирующихся елементов и создать из них список
def create_new_list(list_1, list_2):
     list_repetitive_numbers = []
     lists = list_1 + list_2
     sorted_lists = sorted(lists)
     
     for numbers in sorted_lists:
          numbers_count = sorted_lists.count(numbers)

          if numbers_count >= 2:
               numbers_count = numbers

               list_repetitive_numbers.append(numbers_count)
          
     print(list_repetitive_numbers)

create_new_list([1, 4, 7, 3, 9, 8], [1, 2, 3, 4, 5, 6])



#Преобразование секунд в минуты, часы, дату
import datetime

def second_to_minutes_and_hour(seconds):

     hours = str(datetime.timedelta(seconds=seconds))
     print(hours)

second_to_minutes_and_hour(60)



# Поиск двух слов (самое длинно и часто встречающее) и сохранить их в дикте
def search_words(list_words):
     
     dict_apper_and_lower_words = {}
     dict_repeated_words = {}

     lowew_word = 0
     apper_word = 0
     index_count = 0

     for index_word in range(len(list_words)):

          if index_word >= 2:
               index_count = list_words.count(index_word)
               index_count = index_word
               dict_repeated_words['Repeated word'] = list_words[index_count]

          if len(list_words[index_word]) < len(list_words[lowew_word]):
               lowew_word = index_word
               dict_apper_and_lower_words['Lowew_word'] = list_words[lowew_word]

          elif len(list_words[index_word]) > len(list_words[apper_word]):
               apper_word = index_word
               dict_apper_and_lower_words['Apper_word'] = list_words[apper_word]
    
     print(dict_apper_and_lower_words, dict_repeated_words)

search_words(['qwertyuiop', 'asd', 'asd', 'asdfg', 'zxcvbnm', 'q', 'q', 'zaxsgnhmjaqsw', 'q', 'zaxsgnhmjaqswqwqw'])

