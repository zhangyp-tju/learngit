import kNN_home

def call_kNN_home():
    """test for knn """    
    kNum = 3 # the kNum = 3 is the best maybe
    trainingDataPath = './kNN_trainingDigits'
    testDataPath = './kNN_testDigits'
    kNN_home.testHandWritingClass(trainingDataPath,testDataPath,kNum)

if ( __name__ == "__main__"):

    call_kNN_home()
