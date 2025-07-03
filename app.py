from serpapi import GoogleSearch
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def compare(med_name):
    params = {
    "engine": "google_shopping",
    "q": med_name,
    "api_key": "ab8156db9cfac085d6f411801924f04257e1ee20f7f412df4f8d72cc54b26535",
    "gl":"in"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    shoping_results=results["shopping_results"]
    return shoping_results


c1,c2=st.columns(2)
c1.image('D:\Internship\images.png',width=200)
c2.header('E-pharmacy price comparison system')

# ---------------------------------------------------------------------------------

st.sidebar.title("Enter the name of the medicine:")
med_name=st.sidebar.text_input("Enter Name here 👇:")
number=st.sidebar.text_input("Enter number of options here 👇:")
medcine_comp=[]
med_price=[]

if med_name is not None:
    if st.sidebar.button("price compare"):
        shoping_results=compare(med_name)
        lowest_price=float((shoping_results[0].get('price'))[1:])
        print(lowest_price)
        lowest_price_index=0
        st.sidebar.image(shoping_results[lowest_price_index].get('thumbnail'))
        for i in range(int(number)):
            current_price=float((shoping_results[i].get('price'))[1:])

            medcine_comp.append(shoping_results[i].get('source'))
            med_price.append(float((shoping_results[i].get('price'))[1:]))

            """-----------------------------------------------------------------"""
            st.title(f'Option{i+1}')
            c1,c2=st.columns(2)
            c1.write("Company:")
            c2.write(shoping_results[i].get('source'))

            c1.write("Title:")
            c2.write(shoping_results[i].get('title'))

            c1.write("Price:")
            c2.write(shoping_results[i].get('price'))

            url=shoping_results[i].get('product_link')
            c1.write("Buy link:")
            c2.write("[Link](%s)" % url)
            """-----------------------------------------------"""
            if (current_price<lowest_price):
                lowest_price=current_price
                lowest_price_index=i

        # this is best option code
        st.title("Best Option :")
        c1,c2=st.columns(2)
        c1.write("Company:")
        c2.write(shoping_results[lowest_price_index].get('source'))

        c1.write("Title:")
        c2.write(shoping_results[lowest_price_index].get('title'))

        c1.write("Price:")
        c2.write(shoping_results[lowest_price_index].get('price'))

        url=shoping_results[lowest_price_index].get('product_link')
        c1.write("Buy link:")
        c2.write("[Link](%s)" % url)


        #------------------------------
        #graphs comparisons
        df=pd.DataFrame(med_price,medcine_comp)
        st.title("Chart Comparison :")
        st.bar_chart(df)

        fig,ax=plt.subplots()
        ax.pie(med_price,labels=medcine_comp,shadow=True)
        ax.axis("equal")
        st.pyplot(fig)


        







