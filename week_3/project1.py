Girl_names = ['Evelyn' ,'Jessica' ,'Somto','Edith','Liza','Madonna','Waje','Tola','Aisha','Latifa']
Girl_ages= [17,16,17,18,16,18,17,20,19,17]
Girl_heights = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
Girl_scores = [80,85,70,60,76,66,87,95,50,49]

Boy_names = ['Chinedu','Liam','Wale','Gbenga','Abiola','Kola','Kunle','George','Thomas','Wesley']
Boy_ages = [19,16,18,17,20,19,16,18,17,19]
Boy_heights = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
Boy_scores = [74,87,75,68,66,78,87,98,54,60]
print("Names | Age | Height | scores")
for i in range(len(Girl_names)):
    print(Girl_names[i],'|',Girl_ages[i],'|',Girl_heights[i],'|',Girl_scores[i])

for i in range(len(Boy_names)):
    print(Boy_names[i],'|',Boy_ages[i],'|',Boy_heights[i],'|',Boy_scores[i])