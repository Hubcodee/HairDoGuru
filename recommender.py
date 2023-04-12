from sklearn.preprocessing import normalize,StandardScaler  
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA 
from sklearn.neural_network import MLPClassifier
import pandas as pd
import pickle
# from PIL import Image, ImageDraw,ImageFont
import pandas as pd
import numpy as np
import pathlib
import os
import random
import matplotlib.pyplot as plt
from functions_only_save import make_face_df_save

MODEL = "model.pk1"

#Data Frame
df = pd.DataFrame(columns = ['0','1','2','3','4','5','6','7','8','9','10','11',	'12',	'13',	'14',	'15',	'16','17',
                             '18',	'19',	'20',	'21',	'22',	'23',	'24','25',	'26',	'27',	'28',	'29',
                             '30',	'31',	'32',	'33',	'34',	'35',	'36',	'37',	'38',	'39',	'40',	'41',
                             '42',	'43',	'44',	'45',	'46',	'47',	'48',	'49',	'50',	'51',	'52',	'53',
                             '54',	'55',	'56',	'57',	'58',	'59',	'60',	'61',	'62',	'63',	'64',	'65',
                             '66',	'67',	'68',	'69',	'70',	'71',	'72',	'73',	'74',	'75',	'76',	'77',
                             '78',	'79',	'80',	'81',	'82',	'83',	'84',	'85',	'86',	'87',	'88',	'89',
                             '90',	'91',	'92',	'93',	'94',	'95',	'96',	'97',	'98',	'99',	'100',	'101',
                             '102',	'103',	'104',	'105',	'106',	'107',	'108',	'109',	'110',	'111',	'112',	'113',
                             '114',	'115',	'116',	'117',	'118',	'119',	'120',	'121',	'122',	'123',	'124',	'125',
                             '126',	'127',	'128',	'129',	'130',	'131',	'132',	'133',	'134',	'135',	'136',	'137',
                             '138',	'139',	'140',	'141',	'142',	'143','A1','A2','A3','A4','A5','A6','A7','A8','A9',
                            'A10','A11','A12','A13','A14','A15','A16','Width','Height','H_W_Ratio','Jaw_width','J_F_Ratio',
                             'MJ_width','MJ_J_width'])

style_df = pd.DataFrame(columns = ['face_shape','gender','location','filename','score'])

def process_rec_pics(style_df):
    image_root = r"D:\PROJECTS\IMAGES\recom"
    dir_list = ['heart','long','oval','round','square']
    filenum = 0  
    for gender in ['Female', 'Male']:
        image_dir = image_root + '/' + gender

        for _ in dir_list: 
                sub_dir = [q for q in pathlib.Path(image_dir).iterdir() if q.is_dir()]
                start_j = 0
                end_j = len(sub_dir)
                for j in range(start_j, end_j):
                        for p in pathlib.Path(sub_dir[j]).iterdir():
                            shape_array= []
                            gender = os.path.basename(os.path.dirname(os.path.dirname(p)))
                            face_shape = os.path.basename(os.path.dirname(p)) 
                            sub_dir_file = p
                            face_file_name = os.path.basename(p)

                            shape_array.append(face_shape)
                            shape_array.append(gender)
                            shape_array.append(sub_dir_file)
                            shape_array.append(face_file_name)  
                            
                            random.seed(filenum)  # this keeps the score the same each time I run it
                            rand = random.randint(25,75)  # make a random score to start the rec. engine
                            shape_array.append(rand)

                            style_df.loc[filenum] = np.array(shape_array)

                            filenum += 1
    

def preprocess_data(my_photo:str):
    # Read feature CSV file
    data = pd.read_csv(r'all_features_new.csv',index_col = None)
    data = data.drop('Unnamed: 0',axis = 1)
    data.shape

    # Drop NULL values column
    data_clean = data.dropna(axis=0, how='any')
    X = data_clean
    X = X.drop(['filenum','filename','classified_shape','gender'] , axis = 1)
    X_norm = normalize(X)
    Y = data_clean['classified_shape']

    # Standard Scaling the features
    scaler = StandardScaler()  
    scaler.fit(X)  
    X = scaler.transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,Y,
        test_size=0.25,
        random_state=1200)
    n_components = 18
    pca = PCA(n_components=n_components, svd_solver='randomized',
            whiten=True).fit(X)
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    # #Remove PCA 
    X_train_pca = X_train
    X_test_pca = X_test

    # With best model tuning

    best_mlp = MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
        beta_2=0.999, early_stopping=False, epsilon=1e-08,
        hidden_layer_sizes=(40, 100, 20, 30), learning_rate='constant',
        learning_rate_init=0.01, max_iter=100, momentum=0.9,
        nesterovs_momentum=True, power_t=0.5, random_state=525,
        shuffle=True, solver='sgd', tol=0.0001, validation_fraction=0.1,
        verbose=False, warm_start=False)
    
    model = best_mlp.fit(X_train_pca, Y_train)
    # print(best_mlp.score(X_train_pca, Y_train))
    mlp_score = best_mlp.score(X_test_pca,Y_test)
    # print(mlp_score)
    
    with open(MODEL,'rb') as f:
        model = pickle.load(f)
        
    y_pred = model.predict(X_test_pca)
    mlp_crosstab = pd.crosstab(Y_test, y_pred, margins=True)
    mlp_crosstab
    # print(classification_report(Y_test,y_pred))

    file_num = 2035

    make_face_df_save(my_photo,file_num,df)

    dfc = df
    test_row = dfc.loc[file_num].values.reshape(1,-1)
    test_row = scaler.transform(test_row)  
    # test_shape = best_mlp.predict(test_row)
    test_shape = model.predict(test_row)
    # print(test_shape)
    return test_shape[0]

def run_recommender(uname,gender,filepath):    
    # print("Hello, %s." % uname)
    face_shape_input = preprocess_data(filepath)
    face_shape_input = face_shape_input.lower()
    # print("Face Shape Input: ",face_shape_input)
    process_rec_pics(style_df)

    if gender in ['m', 'M', 'male', 'Male', 'MALE']:
        gender = 'Male'
    else: 
        gender = 'Female'
   
    r = 6
    n_col = 3
    n_row = 2
   
    recommended_df = style_df.loc[(style_df['face_shape'] ==face_shape_input) & (style_df['gender']==gender)].sort_values('score', ascending = 0).reset_index(drop=True)    
    recommended_df = recommended_df.head(r)

    ls = []

    for p in range(0,r):
        res = {}
        idea = str(recommended_df.iloc[p]['location'])
        idea = idea.replace('\\', '/')
        confidence = recommended_df.iloc[p]['score']
        # res[p+1] = { "filename" : idea,"confidence"  : confidence,"face_shape": face_shape_input, "uname":uname}
        res[p+1] = {"filename":idea}
        ls.append(res)        
    # print(ls)
    return ls
    
    # fav = input("Which style is your favorite? ")
    # yuck = input("Which style is your least favorite? ")
    # # update scores based on fav/least fav

    # for row in range(0,r):
    #     fn = recommended_df.at[row,'filename']
    #     srow = style_df.index[style_df['filename'] == fn].tolist()
    #     srow = srow[0]
 
    #     row += 1
    #     if str(row) == str(fav):
    #         style_df.at[srow,'score'] =  style_df.at[srow,'score'] + 5
    #     if str(row) == str(yuck):
    #         style_df.at[srow,'score'] =  style_df.at[srow,'score'] - 5

