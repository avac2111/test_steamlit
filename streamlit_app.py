import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 예측")
st.write("> 보험료 예측해주는 프로그램입니다.")
st.image('https://i.imgur.com/NYfcnki_d.webp?maxwidth=520&shape=thumb&fidelity=high')


# 첫번째 행
r1_col1, r1_col2, r1_col3 = st.columns(3)

age = r1_col1.number_input("age", step=1, value=23)

bmi = r1_col2.number_input("bmi", value=34.40)

children = r1_col3.number_input("children", step=1, value=0)

# 두번째 행
r2_col1, r2_col2, r2_col3 = st.columns(3)

r2_col1.write("smoker")
smoker = r2_col1.checkbox("")

sex_option = ("male", "female")
sex = r2_col2.selectbox("sex", sex_option)
is_male = sex_option[0] == sex

region_option = ('southwest', 'southeast', 'northwest', 'northeast')
region = r2_col3.selectbox("region", region_option)
is_southwest = region_option[0] == region
is_southeast = region_option[1] == region
is_northwest = region_option[2] == region



# 예측 버튼
c01, c02 = st.columns(2)
predict_button = c01.button("예측")
cancel = c02.button("예측 취소")

st.write("---")

# 예측 결과
if predict_button:
    model = joblib.load('first_model.pkl')

    pred = model.predict(np.array([[age, bmi, children, smoker * 1,
        is_male * 1, is_northwest * 1, is_southeast * 1, is_southwest * 1]]))

    if not cancel:
        st.metric("예측 보험료", pred[0])
