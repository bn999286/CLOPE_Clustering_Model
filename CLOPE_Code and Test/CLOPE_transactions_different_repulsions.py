import math
import random
import csv
'''
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
'''

#remove duplicate elements in list
def Remove_Duplicate(duplicate):
    list = []
    for item in duplicate:
        if item not in list:
            list.append(item)
    return list


# update the cluster feature data when adding a transaction
def Delta_Add(cluster, transaction, r):
    # creat a list to store all items of the cluster
    items = []
    j = 0
    while j < len(cluster):
        k = 0
        while k < len(cluster[j]):
            items.append(cluster[j][k])
            k += 1
        j += 1

    # dist_item list stores distint items after removing duplicates items
    dist_items = Remove_Duplicate(items)

    # cluster size
    C_S = len(items)

    # cluster width
    C_W = len(dist_items)

    # number of transactions in cluster
    C_N = len(cluster)

    # initialize S_new and W_new
    S_new = C_S + len(transaction)
    W_new = C_W

    # for each item in transaction
    i = 0
    while i < len(transaction):
        # if occurence of i th item of transaction in cluster is 0
        if (items.count(transaction[i]) == 0):
            # increase the width of the cluster
            W_new += 1
        i += 1

    # print ("W_new = ",  W_new)

    # avoid div =0 when cluster is empty
    div = 0
    if C_W == 0:
        div = 1
    else:
        div = math.pow(C_W, r)

    # return the change of profit
    return S_new * (C_N + 1) / math.pow(W_new, r) - C_S * C_N / div


# find_max_profit_cluster
def Find_Max_Profit_Cluster(transaction, repulsion):
    max_profit = 0
    i_max_profit_cluster = 0

    i = 0
    # for each cluster in clusters
    while i < len(clusters):

        # calculate the change of profit when put transaction in existing cluster
        profit = Delta_Add(clusters[i], transaction, repulsion)
        print("if put t in cluster: ", i,  " -- delta profit =", profit)

        # if profit > max_profit
        if profit > max_profit:
            max_profit = profit
            i_max_profit_cluster = i

        i += 1

    # print the index of max delta profit cluster after appending the transaction
    print("max delta profit at cluster: ", i_max_profit_cluster)
    print("put t in cluster: ", i_max_profit_cluster)
    print("\n")

    # return the index of max profit cluster
    return i_max_profit_cluster


# Phrase 1 - Initialization
def Initialization(dataset, clusters, clusters_index, repulsion):

    print("Phrase 1 - Initialization")

    # set index of cluster with max profit to 0
    i_max_profit_cluster = 0

    i = 0
    # for each transaction in dataset
    while i < len(dataset):

        # print the index of transaction in dataset
        print("t -- ", i)

        # if the index of max profit cluster is large or equal to the index of clusters
        if i_max_profit_cluster >= len(clusters) - 1:
            cluster = []
            clusters.append(cluster)

        # the i th transaction
        transaction = dataset[i]

        # find index of cluster that create maximum profit after add transaction
        i_max_profit_cluster = Find_Max_Profit_Cluster(transaction, repulsion)

        # appenend the transaction in that cluster
        clusters[i_max_profit_cluster].append(transaction)

        # record the location of cluster for transtranction
        clusters_index.append(i_max_profit_cluster)

        i += 1

        # if the last cluster of clusters is empty, remove it
    if len(clusters[len(clusters) - 1]) == 0:
        del clusters[len(clusters) - 1]

    # print(clusters)

    print("\n")


# Phrase 2 - Iterate
def Iterate(dataset, clusters, clusters_index, repulsion):

    print("Phrase 2 - Iterate")

    # set moved = True
    moved = True

    # repeat until moved is False
    while moved:

        i = 0
        moved = False

        # for each transaction in dataset
        k = 0
        while k < len(dataset):

            # print the index of transaction in dataset
            print("t -- ", k)

            # the k-th transaction
            transaction = dataset[k]

            # index of clusters_index
            i_current_cluster = clusters_index[i]

            clusters[i_current_cluster].remove(transaction)

            # find index of cluster that create maximum profit after add transaction
            i_max_profit_cluster = Find_Max_Profit_Cluster(transaction, repulsion)

            # appenend the transaction in that cluster
            clusters[i_max_profit_cluster].append(transaction)

            # if index of max profit cluster is not equal to the #index of clusters_index
            if i_max_profit_cluster != i_current_cluster:
                clusters_index[i] = i_max_profit_cluster
                moved = True

            k += 1

            i += 1



with open('transaction.csv', mode='w') as employee_file:
    writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # read the data and put data in dataset list
    names = ['xiao ming', 'david']
    food1 = ['potato', 'bread', 'banana', 'apple']
    food2 = ['tomato', 'orange', 'egg', 'pizza']
    drink1 = ['milk', 'juice']
    drink2 = ['tea', 'coffee']

    dataset = []

    i = 0
    while i < 2000:

        rand_food_index = 0
        rand_drink_index = 0

        item1 = []
        item2 = []
        item3 = []

        rand_name_index = random.randint(0, len(names) - 1)

        if rand_name_index == 0:
            rand_food_index = random.randint(0, len(food1) - 1)
            rand_drink_index = random.randint(0, len(drink1) - 1)
            item1 = food1[rand_food_index]
            item2 = drink1[rand_drink_index]

        else:
            rand_food_index = random.randint(0, len(food2) - 1)
            rand_drink_index = random.randint(0, len(drink2) - 1)
            item1 = food2[rand_food_index]
            item2 = drink2[rand_drink_index]

        name = names[rand_name_index]

        transaction = []
        transaction.append(name)
        transaction.append(item1)
        transaction.append(item2)

        writer.writerow(transaction)
        dataset.append(transaction)

        i += 1



#remove first item of each transactions because it is class
#record it in the class list
class_list =[]
j=0
while j<len(dataset):
    class_list.append(dataset[j][0])
    del dataset[j][0]
    j+=1


# define a function compute the purity
def Purity(dataset, clusters, class_list):

    purity = 0
    # for each cluster in clusters
    w = 0
    while w < len(clusters):

        # reset num_edibles and the num_poisonous to 0
        num_class1 = 0
        num_class2 = 0

        # for each tansaction in cluster
        y = 0
        while y < len(clusters[w]):

            # the y-th transaction in cluster clusters[w]
            transaction = clusters[w][y]

            #if item in food1
            if transaction[0] in food1:
                num_class1 += 1
            else:
                num_class2 += 1


            # index of transaction in cluster
            y += 1

        # compute the purity by summing up larger one of the num_edibles and the num_poisonous in each cluster
        purity = purity + max(num_class1, num_class2)
        
        # index of cluster in clusters
        w += 1

    return purity



#Cluster transactional data by testing different repulsion values (from 0.5 to 4.0) & compute the number of clusters and purity value
repulsion = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

#num_clusters list stores number of clusters generated for each repulsion
num_clusters_list = []

#purity_list stores purity for each repulsion
purity_list = []

#result_list stores experimental result for each repulsion
result_list = []

m = 0
while m < len(repulsion):

    result = ' '

    r = repulsion[m]
    print("repulsion = ", r,)
    print("-------------------------------------------------------")

    # location of cluster for each transaction
    clusters_index = []

    # empty clusters
    clusters = []

    Initialization(dataset, clusters, clusters_index, r)
    Iterate(dataset, clusters, clusters_index, r)

    # append number of clusters in num_clusters_list
    num_clusters_list.append(len(clusters))

    # append purity in purity list
    empty=[]
    purity_list.append(Purity(empty, clusters, class_list))

    # print number of clusters and purity for each repulsion
    result = "repulsion = ", r, "-- no.clusters = ", len(clusters), "-- purity = ", Purity(dataset, clusters, class_list)

    # print the result for each repulsion
    print(result, "\n\n\n")

    #append result in result list
    result_list.append(str(result))

    m += 1



#print result
#b=0
#while b<len(result_list):

    #print(result_list[b])
    #b+=1


#when clustering finish, print experiment done
print("Experiment done!")

#write the all results in a txt file
file = open("output_transactions_different_repulsions.txt", "w")

n=0
while n<len(result_list):

    file.write(result_list[n])
    file.write("\n")
    n+=1

file.close()



#plot the graph repulsion vs number of clusters, repulsion vs purity
'''
width = .6 # width of a bar

draw = pd.DataFrame({'purity' : purity_list, 'no.clusters' : num_clusters_list})
draw ['purity'].plot(kind='bar', width = width, color="orange")
draw ['no.clusters'].plot(secondary_y=True, marker='o', color='blue')

plt.xlim([-width, len(draw ['purity'])-width])
ax = plt.gca()
ax.set_xticklabels(repulsion)

plt.title('The result of CLOPE on transaction')
plt.show()
'''