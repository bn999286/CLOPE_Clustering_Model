import math
import csv


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

        # calculate the change of profit (delta profit) when put transaction in existing clusters or a new cluster
        profit = Delta_Add(clusters[i], transaction, repulsion)
        print("if put t in cluster: ", i,  " -- delta profit =", profit)

        # if delta profit > delta max_profit
        if profit > max_profit:
            max_profit = profit
            i_max_profit_cluster = i

        i += 1

    #print the index of max delta profit cluster after appending the transaction
    print("max delta profit at cluster: " , i_max_profit_cluster)
    print("put t in cluster: ",i_max_profit_cluster)
    print("\n")

    # return the index of max delta profit cluster after appending the transaction
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

            #print the index of transaction in dataset
            print("t -- ", i)

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

    print("\n")



# define a function compute the purity
def Purity(dataset, clusters, class_list):
    num_edibles = 0
    num_poisonous = 0
    purity = 0

    # for each cluster in clusters
    w = 0
    while w < len(clusters):

        # for each tansaction in cluster
        y = 0
        while y < len(clusters[w]):

            # the y-th transaction in cluster clusters[w]
            transaction = clusters[w][y]

            # for each transaction in dataset
            x = 0
            while x < len(dataset):

                # if tansaction in cluster equal to the transaction in dataset
                if transaction == dataset[x]:

                    if class_list[x] == 'e':
                        num_edibles += 1
                    else:
                        num_poisonous += 1

                # index of transaction in dataset
                x += 1

            # index of transaction in cluster
            y += 1

        # compute the purity by summing up larger one of the num_edibles and the num_poisonous in each cluster
        purity = purity + max(num_edibles, num_poisonous)

        # reset num_edibles and the num_poisonous to 0
        num_edibles = 0
        num_poisonous = 0

        # index of cluster in clusters
        w += 1

    return purity



#read the data and put data in dataset list
dataset = []
a=0
with open("mushrooms.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # each row is a list
        dataset.append(row)
        a+=1



#remove first item of each transactions because it is class
#record it in the class list
class_list =[]
j=0
while j<len(dataset):
    class_list.append(dataset[j][0])
    del dataset[j][0]
    j+=1



#make attribute values in each tarnsaction distinct
transaction_size =len(dataset[0])
m=0
while m<transaction_size:
    n=0
    while n<len(dataset):
        dataset[n][m]= dataset[n][m] +str(m)
        n+=1
    m+=1


#remove missing value ='?10' of the transactions in dataset
ignore=0
a=0
while a<len(dataset) :
    if'?10' in dataset[a]:
        dataset[a].remove('?10')
        ignore+=1
    a+=1




#the list of cluster index for each transaction
clusters_index=[]

#empty list of clusters
clusters = []

#type the repulsion value
repulsion = float(input ("Please enter the repulsion: "))

#run the CLOPE
Initialization (dataset, clusters, clusters_index, repulsion)
Iterate(dataset, clusters, clusters_index, repulsion)



#when clustering is finish, print experiment done
print("Experiment done!")


#write the experimental result in a txt file
file = open("output_repulsion.txt", "w")

file.write("When repulsion = ")
file.write(str(repulsion))
file.write(" : ")
file.write("\n")

#the number of clusters has created
file.write("number of clusters = ")
file.write(str(len(clusters)))
file.write("\n")

#purity
file.write("purity = ")
file.write(str(Purity(dataset, clusters, class_list)))
file.write("\n")

#the list of cluster index for each transaction
file.write("cluster index for each transaction: ")
file.write("\n")
file.write(str(clusters_index))
file.write("\n")

file.close()

