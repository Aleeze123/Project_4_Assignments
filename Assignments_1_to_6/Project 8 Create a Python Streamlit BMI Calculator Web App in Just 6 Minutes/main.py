import streamlit as st
from termcolor import colored
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "You are underweight."
    elif 18.5 <= bmi < 24.9:
        return "You have a normal weight."
    elif 25 <= bmi < 29.9:
        return "You are overweight."
    else:
        return "You are obese."
def main():
    st.title("BMI Calculator 🏋️‍♀️")
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=500.0, step=0.1)
    height = st.number_input("Enter your height (meters):", min_value=0.5, max_value=3.0, step=0.01)
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        
        st.write(f"Your BMI is: **{bmi:.2f}**")
        interpretation = interpret_bmi(bmi)
        st.write(interpretation)
        if bmi < 18.5:
            st.warning("You are underweight. Consider consulting a healthcare provider.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight. Keep up the good work!")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight. Consider adopting a healthier lifestyle.")
        else:
            st.error("You are obese. Please consult a healthcare provider for guidance.")

if __name__ == "__main__":
    main()
