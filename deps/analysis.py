from sklearn.cluster import KMeans

#in this method i'm just renaming the needed columns and deleting the undesirable columns
def remove_columns(cs_df):

    cs_df.drop(["SKUS"],axis=1, inplace=True)
    cs_df.drop(['عنوان العميل'],axis = 1, inplace=True)
    cs_df.drop([' (غير مفعلة) رابط موقع العميل على الخريطة'],axis = 1, inplace=True)
    cs_df.drop(['رقم البوليصة'],axis=1, inplace=True)
    cs_df.drop(['حالة الطلب'],axis=1, inplace=True)
    cs_df.drop(['المدينة'],axis=1, inplace=True)
    cs_df.drop(['الخصم'],axis=1, inplace=True)
    cs_df.drop(['تكلفة الشحن'],axis=1, inplace=True)
    cs_df.drop(['طريقة الدفع '],axis=1, inplace=True)
    cs_df.drop(['عمولة الدفع عند الاستلام'],axis=1, inplace=True)
    cs_df.drop(['الضريبة'],axis=1, inplace=True)
    cs_df.drop(['شركة الشحن / الفرع'],axis=1, inplace=True)

    cs_df.rename(columns = {'رقم الطلب':'InvoiceNo'}, inplace=True)
    cs_df.rename(columns = {'اسم العميل':'CustomerID'}, inplace=True)
    cs_df.rename(columns = {'مجموع السلة':'amount'}, inplace=True)
    cs_df.rename(columns = {'تاريخ الطلب':'InvoiceDate'}, inplace=True)


def k_mean(X_scaled):
    cl = 10
    corte = 0.1

    anterior = 100000000000000
    cost = [] 
    K_best = cl

    for k in range (1, cl+1):
        # Create a kmeans model on our data, using k clusters.  random_state helps ensure that the algorithm returns the same results each time.
        model = KMeans(
            n_clusters=k, 
            init='k-means++', #'random',
            n_init=10,
            max_iter=300,
            tol=1e-04,
            random_state=101)

        model = model.fit(X_scaled)

        # These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
        labels = model.labels_
    
        # Sum of distances of samples to their closest cluster center
        interia = model.inertia_
        if (K_best == cl) and (((anterior - interia)/anterior) < corte): K_best = k - 1
        cost.append(interia)
        anterior = interia



    # Create a kmeans model with the best K.
    model = KMeans(n_clusters=K_best, init='k-means++', n_init=10,max_iter=300, tol=1e-04, random_state=101)

    # Note I'm scaling the data to normalize it! Important for good results.
    model = model.fit(X_scaled)

    # These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
    return model