import streamlit as st

st.sidebar.header("Content Formater ")


location = st.sidebar.selectbox('Select the location', ['Kathmandu', 'Dharan', 'Birtamode'])
st.markdown(''' 
    ### Content will be generated of: ''')
st.write(location)

Status = st.sidebar.text_area('Write content here:') 

links  = st.sidebar.text_area('paste product link:') 

B_link = st.sidebar.text_area('Enter brand link for viber community (kathmandu) :')


st.markdown(''' ### Double check the content for any error: ''')
st.write(Status)

st.markdown(''' ### Product URL's:''')
st.code(links)


st.markdown(''' ### Result ::''')

st.markdown(''' ##### For Facebook ''')

if location == 'Kathmandu':
    st.code(Status+"\n\nSTAY HOME 🏠 STAY SAFE😷 SHOP ONLINE 🛒 \n\n"+links+"\n\n\nEnjoy the biggest discounts and offers ever on groceries purchased online. 🛒🛒. \n\n✅No minimum order \n\n✅Discounts up to 20% \n\n✅2% cashback on eSewa payment \n\n✅Maximum delivery charge Rs. 50 \n\n✅Free Home Delivery above cart value of Rs. 1000 \n\n✅One lucky customer can win One plus Nord N100 Phone \n\n\nConditions:\n\n👉 Products available within Kathmandu Valley only\n\n✅Pay online, the swipe of a card at delivery is also available. We take cash on delivery but prefer not to.\n\nCall us on 📱9880123123 or Inbox us for any inquiry.\n\n#onlineshopping #saathimart #onlinebusiness #retail  #franchise \n\n#o2o #TogetherForChange #onlineshop #shoplocal #groceries  #lockdown #essentials")
elif location == 'Birtamode':
    st.code(Status+"\n\nIf you are from Birtamode please place your order after choosing your location as Birtamode for faster delivery.\n\nOr Click the link >>>> "+links+ "\n\n\nSTAY HOME 🏠 STAY SAFE😷 SHOP ONLINE 🛒\n\n\nThe products, which are available for delivery in Birtamode have a label on them, which states “Saathimart Delivering inside Birtamode only”.\n\n\nEnjoy the biggest discounts and offers ever on grocery purchased online 🛒🛒.\n\n✅No minimum order \n\n✅Discounts up to 20% \n\n✅2% cashback on eSewa payment \n\n✅Maximum delivery charge Rs. 50 \n\n✅Free Home Delivery above cart value of Rs. 1000 \n\n✅One lucky customer can win One plus Nord N100 Phone \n\n\nConditions:\n\n👉Pay online or we also take cash on delivery\n\n\nCall us on 📱9880123123 or Inbox us for any inquiry.\n\n#onlineshopping #saathimart #onlinebusiness #retail  #franchise \n\n#o2o #TogetherForChange #onlineshop #shoplocal #groceries  #lockdown #essentials")  
else:
    st.code(Status+"\n\nIf you are from Dharan, please place your order after choosing your location as Dharan for faster delivery.\n\nOr Click the link >>>> "+links+ "\n\n\nSTAY HOME 🏠 STAY SAFE😷 SHOP ONLINE 🛒\n\n\nThe products, which are available for delivery in Dharan have a label on them, which states “Saathimart Delivering inside Dharan only”.\n\n\nEnjoy the biggest discounts and offers ever on grocery purchased online 🛒🛒.  \n\n✅No minimum order \n\n✅Discounts up to 20% \n\n✅2% cashback on eSewa payment \n\n✅Maximum delivery charge Rs. 50 \n\n✅Free Home Delivery above cart value of Rs. 1000 \n\n✅One lucky customer can win One plus Nord N100 Phone \n\n\nConditions:\n\n👉Pay online or we also take cash on delivery\n\n\nCall us on 📱9880123123 or Inbox us for any inquiry.\n\n#onlineshopping #saathimart #onlinebusiness #retail  #franchise \n\n#o2o #TogetherForChange #onlineshop #shoplocal #groceries  #lockdown #essentials")


st.markdown(''' ### Result ::''')

st.markdown(''' ##### For Instagram ''')

if location == 'Kathmandu':
    st.code(Status+"\n\nSTAY HOME 🏠 STAY SAFE😷 SHOP ONLINE 🛒 \n\n✔️To shop online please find the link in the bio. \n\n\nEnjoy the biggest discounts and offers ever on groceries purchased online. 🛒🛒. \n\n✅No minimum order \n\n✅Discounts up to 20% \n\n✅2% cashback on eSewa payment \n\n✅Maximum delivery charge Rs. 50 \n\n✅Free Home Delivery above cart value of Rs. 1000 \n\n✅One lucky customer can win One plus Nord N100 Phone \n\n\nConditions:\n\n👉 Products available within Kathmandu Valley only\n\n✅Pay online, the swipe of a card at delivery is also available. We take cash on delivery but prefer not to.\n\nCall us on 📱9880123123 or DM us for any inquiry.\n\n#onlineshopping #saathimart #onlinebusiness #retail  #franchise \n\n#o2o #TogetherForChange #onlineshop #shoplocal #groceries  #lockdown #essentials")
elif location == 'Birtamode':
    st.code(Status+"\n\nIf you are from Birtamode, please place your order after choosing your location as Birtamode for faster delivery.\n\n\nSTAY HOME 🏠 STAY SAFE😷 SHOP ONLINE 🛒 \n\n✔️To shop online please find the link in the bio.\n\n\nThe products, which are available for delivery in Birtamode, have a label on them, which states “Saathimart Delivering inside Birtamode only”.\n\n\nEnjoy the biggest discounts and offers ever on groceries purchased online. 🛒🛒. \n\n✅No minimum order \n\n✅Discounts up to 20% \n\n✅2% cashback on eSewa payment \n\n✅Maximum delivery charge Rs. 50 \n\n✅Free Home Delivery above cart value of Rs. 1000 \n\n✅One lucky customer can win One plus Nord N100 Phone\n\n👉Pay online or we also take cash on delivery\n\nCall us on 📱9880123123 or DM us for any inquiry.\n\n#onlineshopping #saathimart #onlinebusiness #retail  #franchise \n\n#o2o #TogetherForChange #onlineshop #shoplocal #groceries  #lockdown #essentials") 
else:
    st.code(Status+"\n\nIf you are from Dharan, please place your order after choosing your location as Dharan for faster delivery.\n\n\nSTAY HOME 🏠 STAY SAFE😷 SHOP ONLINE 🛒 \n\n✔️To shop online please find the link in the bio.\n\n\nThe products, which are available for delivery in Dharan, have a label on them, which states “Saathimart Delivering inside Dharan only”.\n\n\nEnjoy the biggest discounts and offers ever on groceries purchased online. 🛒🛒. \n\n✅No minimum order \n\n✅Discounts up to 20% \n\n✅2% cashback on eSewa payment \n\n✅Maximum delivery charge Rs. 50 \n\n✅Free Home Delivery above cart value of Rs. 1000 \n\n✅One lucky customer can win One plus Nord N100 Phone\n\n👉Pay online or we also take cash on delivery\n\nCall us on 📱9880123123 or DM us for any inquiry.\n\n#onlineshopping #saathimart #onlinebusiness #retail  #franchise \n\n#o2o #TogetherForChange #onlineshop #shoplocal #groceries  #lockdown #essentials")  

# for viber

st.markdown(''' ### Result ::''')

st.markdown(''' ##### For Viber Community ''')

if location == 'Kathmandu':
    st.code(Status+"\n\nShop Now >>>>"+B_link) 
elif location == 'Birtamode':
    st.code(Status+"\n\nShop Now >>>> https://bit.ly/35KG0cR") 
else:
    st.code(Status+"\n\nShop Now >>>> https://bit.ly/35Xeyci") 


