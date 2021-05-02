import streamlit as st
import pandas as pd
from display_utils import *


st.image('vanti_dark.png')
# App title
st.title("Display Book")
st.subheader('by convention: Positive = "Fail", Negative = "Pass"')



# Image source selection
stages = ['WP2_CM_MEAS_FIB',
          'FSGB_VE_MEAS_FIB',
          'HC_PL',
          'RWHM_VE',
          'SCAP_VE']



metrics = ['True Positive','False Positive','True Negative','False Negative']


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.text('select stage:')
stage = st.radio('', stages)
st.text('select metric:')
metric = st.radio('', metrics)

if metric == 'True Positive':
    metric = 'TP'
if metric == 'True Negative':
    metric = 'TN'
if metric == 'False Positive':
    metric = 'FP'
if metric == 'False Negative':
    metric = 'FN'

# plot_stage_matrix(stages[2], N = 25)
plot_stage_matrix_one(stage, N=12, metric=metric, save_flag = True)
st.image('output.png')

# if option == 'Choose a test image':
#     a = 1
#     # # Test image selection
#     # test_images = os.listdir('model/data/test/')
#     # test_image = st.selectbox(
#     #     'Please select a test image:', test_images)
#     #
#     # # Read the image
#     # file_path = 'model/data/test/' + test_image
#     # img = open_image(file_path)
#     #
#     # # Get the image to display
#     # display_img = mpimg.imread(file_path)
#     # # Predict and display the image
#     # predict(model, img, display_img, interp=interp)
#
# elif option == 'Choose your own image':
#     a = 1
#     # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "BMP"])
#     # if uploaded_file is not None:
#     #     img_pil = PIL.Image.open(uploaded_file)
#     #     img_tensor = T.ToTensor()(img_pil)
#     #     img = Image(img_tensor)
#     #
#     #     pred_class, pred_prob = predict(model, img, display_img=uploaded_file)
#     #     # st.write('%s (%.2f%%)' % (pred_class, pred_prob))
#
# else:
#     url = st.text_input("Please input a url:")
#     #
#     # if url != "":
#     #     try:
#     #         # Read image from the url
#     #         response = requests.get(url)
#     #         pil_img = PIL.Image.open(BytesIO(response.content))
#     #         display_img = np.asarray(pil_img)  # Image to display
#     #
#     #         # Transform the image to feed into the model
#     #         img = pil_img.convert('RGB')
#     #         img = image.pil2tensor(img, np.float32).div_(255)
#     #         img = image.Image(img)
#     #
#     #         # Predict and display the image
#     #         predict(img, display_img)
#     #
#     #     except:
#     #         st.text("Invalid url!")
#
#
