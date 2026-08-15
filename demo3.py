import streamlit as st

st.title("welcome streamlit")
st.header("this is header")
st.subheader("this is subheader")
formula = ''' a+b '''
st.latex(formula)
python_code = '''
     a = 9
     b=4
     c=78
     v = a+b+c
     print(v)

    '''
st.code(python_code, language='python')
st.header("Python")
st.caption("python is good lang ")

st.subheader("checkbox")
st.caption("click the button below")
agree = st.checkbox("agree",value=True)
ml = st.checkbox("machine")
if agree:
  st.write("yes")
if ml:
    st.write("yes machine learning")
st.header('radio')
radio_button= st.radio(("what is your fav color ?"),('white','yellow','blue','red'))
st.write('your fav color is ', radio_button)
st.header('selectbox')
select_box= st.selectbox(("what is your fav color ?"),('white','yellow','blue','red'))
st.write('your fav color is ', select_box)
st.header('Multiple selectbox')
select_box= st.multiselect(("what is your fav color ?"),['white','yellow','blue','red'])
st.write('your fav color is ', select_box)
st.subheader("slider")
salary_range  = st.slider("what is the  range of salary you expect ?", 0,100000,1000)
st.write('your salary range is ', salary_range)
st.subheader("text-input")
with st.container():
    name =st.text_input('name')
    age=st.number_input('age' , min_value=0,max_value=100,value=15,step=1)
    description = st.text_area('description')
    dob=st.date_input('dob')
    submit = st.button("submit info")
    if submit:
        info_dict = {
         'name':name,
         'age':age,
         'description':description,
         'dob':dob
        }
        st.write(info_dict)


import streamlit as st
import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np

# Train a model
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model with joblib.dump
joblib.dump(model, "model.joblib")
# Load model
model = joblib.load("model.joblib")       #< -- load



# Streamlit UI
st.title("🌸 Iris Flower Prediction App")
st.write("Enter flower measurements to predict species")

# User inputs
sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
sepal_width  = st.number_input("Sepal Width", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
petal_width  = st.number_input("Petal Width", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.success(f"🌼 Predicted Species: {prediction}")