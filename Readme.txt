CLOPE Clustering Algorithm

***************************************************************************************
Mushrooms experiment from article (mushrooms.csv): 
1.CLOPE_mushrooms_type_repulsion.py
Execution command: python CLOPE_mushrooms_type_repulsion.py
------------------------------------------------------------------------------------------------------
This program clusters mushroom dataset by asking user to type a repulsion value. Then the program will run and output experimental result in a txt file "output_repulsion.txt". The result  includes the number of clusters has created, purity value and the list of cluster index for each mushroom (or transaction). During the execution, the terminal will print the clustering process for each mushroom, and final clusters list for each repulsion. The total running time for repulsion = 0.5 is around 30 minutes. 


2.CLOPE_mushrooms_different_repulsions.py
Execution command: python CLOPE_mushrooms_different_repulsions.py
------------------------------------------------------------------------------------------------------
This program clusters mushroom dataset by setting different repulsion from 0.5 to 4, and computes the number of clusters and purity value for each repulsion. The final experimental result (see the will be written in "output_different_repulsions.txt". During the execution, the terminal will print the clustering process information for each mushroom, and number of clusters and purity for each repulsion. The running time for this code is very long (around 6 hrs) due to big data doing 8 clustering on 8,124 mushrooms with different repulsion values (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4). If you want to see the general execution of this code, I recommend to reduce the data size, or instead run the tester program CLOPE_transactions_different_repulsions.py program that’s described below (runtime of 2-3 minutes for all values of repulsion).


***************************************************************************************
Transactional dataset created by ourselves.
CLOPE_transactions_different_repulsions.py
Execution command: python CLOPE_transactions_different_repulsions.py
------------------------------------------------------------------------------------------------------
This program firstly randomly generates a transactional data set (The dataset has 2,000 samples, 2 classes(names). Each sample has 2 attributes(items). The csv file will also be automatically created) then clusters the data set by setting different repulsion from 0.5 to 4, and computes the number of clusters and purity value for each repulsion. The final experimental result will be written in "output_transactions_different_repulsions.txt". During the execution, the terminal will print the clustering process information for each transaction, and number of clusters and purity for each repulsion. Runtime for all values of repulsion is about 2-3 minutes (much smaller dataset than mushrooms).  

