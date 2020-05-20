list_of_words = ["hello","Hi","bye","last"]
# with_deliminator = ""
# for word in list_of_words:
#     with_deliminator += word + ","
# print(with_deliminator)

deliminator = ","
temp = deliminator.join(list_of_words)
print(temp)