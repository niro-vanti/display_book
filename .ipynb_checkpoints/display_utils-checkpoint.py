import pandas as pd
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import numpy as np
from IPython.display import Image


def get_top_n(df, N=25):
    df = df[df['train \ test'] == 1]

    if df.shape[0] > N:
        randomlist = random.sample(range(0, df.shape[0]), N)
        return df.iloc[randomlist, :]
    else:
        return df


def get_good_bad(df, N=25):
    GOOD_list = df[df.label == 0]
    BAD_list = df[df.label == 1]

    tn_list = GOOD_list[GOOD_list.vanti == 0]
    fp_list = GOOD_list[GOOD_list.vanti == 1]
    tp_list = BAD_list[BAD_list.vanti == 1]
    fn_list = BAD_list[BAD_list.vanti == 0]

    tn_list = get_top_n(tn_list, N=N)
    fp_list = get_top_n(fp_list, N=N)
    tp_list = get_top_n(tp_list, N=N)
    fn_list = get_top_n(fn_list, N=N)

    return tn_list, fp_list, tp_list, fn_list


def get_image_list(folder_name, List):
    images = []
    vanti_label = []
    real_label = []
    test_label = []
    for i in range(List.shape[0]):
        try:
            images.append(mpimg.imread('../US_Testing/' + folder_name + '/' + List['file name'].iloc[i]))
            q = List['vanti'].iloc[i]
            b = List['label'].iloc[i]
            t = List['score'].iloc[i]
            test_label.append(t)
            if b == 0:
                real_label.append('GOOD')
            else:
                real_label.append('BAD')
            if q == 0:
                vanti_label.append('GOOD')
            else:
                vanti_label.append('BAD')
        except:
            print(List['file name'].iloc[0], ' not found')
    return images, vanti_label, real_label, test_label


def plot_image_matrix(images, vanti_label, real_label, test_label, name):
    plt.figure(figsize=(25, 25))
    columns = 4

    agg_image = np.zeros(images[0].shape)

    for i, image in enumerate(images):
        v = vanti_label[i]
        r = real_label[i]
        t = test_label[i]
        S = name + ': Real = ' + r + ' Vanti = ' + v + ' (score = ' + str(np.round(t, 2)) + ')'

        agg_image = agg_image + image

        plt.subplot(len(images) / columns + 1, columns, i + 1)
        plt.subplots_adjust(bottom=5, top=6)
        plt.title(S)
        plt.imshow(image)

    agg_image = agg_image / i
    plt.imshow(image)
    plt.title('agg_image')


def plot_stage_matrix(stage_name, N=25):
    df = pd.read_csv('seagate_results_directory - ' + stage_name + '.csv')

    print(stage_name)
    print('-------------------------------------------------- ')
    print(df.label.value_counts())

    tn_list, fp_list, tp_list, fn_list = get_good_bad(df, N=N)
    tn_images, tn_vanti_label, tn_real_label, tn_test_label = get_image_list(stage_name, tn_list)
    tp_images, tp_vanti_label, tp_real_label, tp_test_label = get_image_list(stage_name, tp_list)
    fn_images, fn_vanti_label, fn_real_label, fn_test_label = get_image_list(stage_name, fn_list)
    fp_images, fp_vanti_label, fp_real_label, fp_test_label = get_image_list(stage_name, fp_list)

    plot_image_matrix(tp_images, tp_vanti_label, tp_real_label, tp_test_label, name='TP')
    plot_image_matrix(tn_images, tn_vanti_label, tn_real_label, tn_test_label, name='TN')
    plot_image_matrix(fn_images, fn_vanti_label, fn_real_label, fn_test_label, name='FN')
    plot_image_matrix(fp_images, fp_vanti_label, fp_real_label, fp_test_label, name='FP')

#     Image(filename='test.png') 