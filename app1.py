# Streamlit frontend
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# streamlit webpage design
st.set_page_config(page_title= "Phonepe",
                   page_icon= "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/phonepe-logo-icon.png",
                   layout= "wide")
page_bg_img = """
<style>
body {
    background-image: url("https://cdn.pixabay.com/photo/2014/06/16/23/39/black-370118_640.png");
    background-size: cover;
}
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn.pixabay.com/photo/2014/06/16/23/39/black-370118_640.png");
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
[data-testid="stToolbar"] {
    right: 5rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("data:image/png;base64");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit sidebar design
with st.sidebar:
    selected = option_menu("Menu", ["Home","Top Charts","Explore Data","My-Profile"], 
                icons=["house","graph-up-arrow","bar-chart-line", "list-task"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#9a78eb"},
                        "nav-link-selected": {"background-color": "#5d78a3"}})

# Home design Description
if selected == "Home":
    st.markdown("# :rainbow[Data Visualization and Exploration]")
    st.markdown("## :grey[A User-Friendly Tool Using Streamlit and Plotly]")
    col1,col2 = st.columns([3,2],gap="medium")
    with col1:
        st.markdown("### :grey[Technologies used : ]:blue[Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.]")
        st.markdown("### :grey[Overview : ]:blue[In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.]")
        st.write(" ")
        st.write(" ")
        st.image("27736-temp-02-2-2.png")
        
if selected == "Top Charts":
    st.markdown("## :green[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year=st.selectbox('**Year**',('2018','2019','2020','2021','2022'))
        Quarter=st.selectbox('**Quarter**',('1','2','3','4'))
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """
                )
    
    if Type == "Transactions":
        col1, col2, col3 = st.columns([1, 1, 1], gap="small")

        with col1:
            st.markdown("### :green[Top 10 State]")
            aggregated_trans_df = pd.read_csv('Aggregated_Trans.csv')

            # Filter data based on selected Year and Quarter
            filtered_trans_df = aggregated_trans_df[(aggregated_trans_df['Year'] == int(Year)) & (aggregated_trans_df['Quarter'] == int(Quarter))]

            # Group by 'State' and aggregate
            grouped_trans_df = filtered_trans_df.groupby('State').agg({
                'Transaction_count': 'sum',
                'Transaction_amount': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'Transaction_amount' column in descending order and selecting the top 10
            result_df = grouped_trans_df.sort_values(by='Transaction_amount', ascending=False).head(10)

            # Creating a DataFrame with the required columns
            df = pd.DataFrame(result_df, columns=['State', 'Transaction_count', 'Transaction_amount'])

            # Creating a pie chart using Plotly Express
            fig = px.pie(df, values='Transaction_amount',
                        names='State',
                        color_discrete_sequence=px.colors.sequential.Viridis,
                        hover_data=['Transaction_count'],
                        labels={'Transaction_count': 'Total_Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')

            # Displaying the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### :green[Top 10 District]")
            map_trans_df = pd.read_csv('Map_Trans.csv')

            # Filter data based on selected Year and Quarter
            filtered_map_trans_df = map_trans_df[(map_trans_df['Year'] == int(Year)) & (map_trans_df['Quarter'] == int(Quarter))]

            # Group by 'District' and aggregate
            grouped_map_trans_df = filtered_map_trans_df.groupby('District').agg({
                'Count': 'sum',
                'Amount': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'Amount' column in descending order and selecting the top 10
            result_df = grouped_map_trans_df.sort_values(by='Amount', ascending=False).head(10)
            df = pd.DataFrame(result_df, columns=['District', 'Count', 'Amount'])

            # Creating a pie chart using Plotly Express
            fig = px.pie(df, values='Amount',
                        names='District',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Count'],
                        labels={'Count': 'Total_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')

            # Displaying the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            st.markdown("### :green[Top 10 Pincode]")
            top_trans_df = pd.read_csv('Top_Trans_data.csv')

            # Filter data based on selected Year and Quarter
            filtered_top_trans_df = top_trans_df[(top_trans_df['Year'] == int(Year)) & (top_trans_df['Quarter'] == int(Quarter))]

            # Group by 'Pincode' and aggregate
            grouped_top_trans_df = filtered_top_trans_df.groupby('Pincode').agg({
                'Transaction_count': 'sum',
                'Transaction_amount': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'Transaction_amount' column in descending order and selecting the top 10
            result_df = grouped_top_trans_df.sort_values(by='Transaction_amount', ascending=False).head(10)

            # Creating a DataFrame with the required columns
            df = pd.DataFrame(result_df, columns=['Pincode', 'Transaction_count', 'Transaction_amount'])

            # Creating a pie chart using Plotly Express
            fig = px.pie(df, values='Transaction_amount',
                        names='Pincode',
                        color_discrete_sequence=px.colors.sequential.Viridis,
                        hover_data=['Transaction_count'],
                        labels={'Transaction_count': 'Total_Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')

            # Displaying the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

  
# --------------------------------------------------------------------------------------
    if Type == "Users":
        col1,col2,col3,col4 = st.columns([2,2,2,2],gap="small")
        
        with col1:
            st.markdown("### :green[Brands]")
            if Year == 2022 and Quarter in [2, 3, 4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                # Assuming you have a DataFrame named 'aggregate_user_df' with the necessary columns
                aggregate_user_df = pd.read_csv('Aggregated_User.csv')

                # Filter data based on selected Year and Quarter
                filtered_user_df = aggregate_user_df[(aggregate_user_df['Year'] == int(Year)) & (aggregate_user_df['Quarter'] == int(Quarter))]

                # Group by 'Brands' and aggregate
                grouped_user_df = filtered_user_df.groupby('Brands').agg({
                    'Count': 'sum',
                    'Percentage': 'mean'
                }).reset_index()

                # Sorting the DataFrame by 'total_user_count' column in descending order and selecting the top 10
                result_df = grouped_user_df.sort_values(by='Count', ascending=False).head(10)

                # Creating a bar chart using Plotly Express
                fig = px.bar(
                    result_df,
                    title='Top 10 User Brands',
                    x="Count",
                    y="Brands",
                    orientation='h',
                    color=result_df['Percentage'] * 100,
                    color_discrete_sequence=px.colors.sequential.Viridis)

                fig.update_layout(xaxis_title='Total User Count', yaxis_title='User Brand')
                st.plotly_chart(fig, use_container_width=True)
        with col2:
            df_user = pd.read_csv('Map_user_data.csv')

            # Filter data based on selected Year and Quarter
            filtered_user_df = df_user[(df_user['Year'] == int(Year)) & (df_user['Quarter'] == int(Quarter))]

            # Overall District Data - User App Opening Frequency
            st.markdown("### :green[District]")

            # Group by 'District' and aggregate
            grouped_user_df = filtered_user_df.groupby('District').agg({
                'RegisteredUser': 'sum',
                'AppOpens': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'RegisteredUser' column in descending order and selecting the top 10
            result_df = grouped_user_df.sort_values(by='RegisteredUser', ascending=False).head(10)

            # Creating a bar chart using Plotly Express
            fig_user_district = px.bar(
                result_df,
                title='Top 10 District',
                x='RegisteredUser',
                y='District',
                orientation='h',
                color='RegisteredUser',
                color_continuous_scale=px.colors.sequential.Agsunset
            )

            st.plotly_chart(fig_user_district, use_container_width=True)
              
        with col3:
            df_top_user = pd.read_csv('Top_User_data.csv')

            # Filter data based on selected Year and Quarter
            filtered_top_user_df = df_top_user[(df_top_user['Year'] == int(Year)) & (df_top_user['Quarter'] == int(Quarter))]

            # Overall Pincode Data - User App Opening Frequency
            st.markdown("### :green[Pincode]")

            # Group by 'Pincode' and aggregate
            grouped_top_user_df = filtered_top_user_df.groupby('Pincode').agg({
                'RegisteredUsers': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'RegisteredUsers' column in descending order and selecting the top 10
            result_df = grouped_top_user_df.sort_values(by='RegisteredUsers', ascending=False).head(10)

            # Creating a pie chart using Plotly Express
            fig_top_user_pie = px.pie(
                result_df,
                values='RegisteredUsers',
                names='Pincode',
                title='Top 10',
                color_discrete_sequence=px.colors.sequential.Viridis,
                hover_data=['RegisteredUsers']
            )

            fig_top_user_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_top_user_pie, use_container_width=True)
                    
        with col4:
            df_map_user = pd.read_csv('Map_user_data.csv')

            # Filter data based on selected Year and Quarter
            filtered_map_user_df = df_map_user[(df_map_user['Year'] == int(Year)) & (df_map_user['Quarter'] == int(Quarter))]

            # Overall State Data - User App Opening Frequency
            st.markdown("### :green[State]")

            # Group by 'State' and aggregate
            grouped_map_user_df = filtered_map_user_df.groupby('State').agg({
                'RegisteredUser': 'sum',
                'AppOpens': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'RegisteredUser' column in descending order and selecting the top 10
            result_df = grouped_map_user_df.sort_values(by='RegisteredUser', ascending=False).head(10)

            # Creating a pie chart using Plotly Express
            fig_map_user_pie = px.pie(
                result_df,
                values='RegisteredUser',
                names='State',
                title='Top 10',
                color_discrete_sequence=px.colors.sequential.Agsunset,
                hover_data=['AppOpens'],
                labels={'AppOpens': 'Total_Appopens'}
            )

            fig_map_user_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_map_user_pie, use_container_width=True)

if selected == "Explore Data":
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2022)
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
    
    col1,col2= st.columns(2)   
     #EXPLORE DATA - Transactions   
    if Type == "Transactions":
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        with col1:
            st.markdown("## :violet[Overall State Data - Transactions Amount]")
            
            # Reading Map_Trans.csv and state_names.csv
            map_trans_df = pd.read_csv('Map_Trans.csv')
            state_names_df = pd.read_csv('state_names.csv')
            
            # Filtering data based on selected Year and Quarter
            filtered_map_trans_df = map_trans_df[(map_trans_df['Year'] == int(Year)) & (map_trans_df['Quarter'] == int(Quarter))]
            
            # Group by 'State' and aggregate
            grouped_map_trans_df = filtered_map_trans_df.groupby('State').agg({
                'Count': 'sum',
                'Amount': 'sum'
            }).reset_index()

            # Merging with state_names_df to get the state names
            grouped_map_trans_df['state'] = state_names_df['state']
            
            # Creating choropleth map using Plotly Express
            fig = px.choropleth(grouped_map_trans_df, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='state',
                                color='Amount',
                                color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)


        # Overall State Data - TRANSACTIONS count - INDIA MAP
        with col2:
            st.markdown("## :violet[Overall State Data - Transactions count]")
            
            # Reading Map_Trans.csv and state_names.csv
            map_trans_df = pd.read_csv('Map_Trans.csv')
            state_names_df = pd.read_csv('state_names.csv')
            
            # Filtering data based on selected Year and Quarter
            filtered_map_trans_df = map_trans_df[(map_trans_df['Year'] == int(Year)) & (map_trans_df['Quarter'] == int(Quarter))]
            
            # Group by 'State' and aggregate
            grouped_map_trans_df = filtered_map_trans_df.groupby('State').agg({
                'Count': 'sum',
                'Amount': 'sum'
            }).reset_index()

            # Merging with state_names_df to get the state names
            
            grouped_map_trans_df['state'] = state_names_df['state']
            # Creating choropleth map using Plotly Express
            fig = px.choropleth(grouped_map_trans_df, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='state',
                                color='Count',  # Using 'Count' for Total_Transactions
                                color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)
        # BAR CHART - TOP PAYMENT TYPE
        with col1:
            # BAR CHART - TOP PAYMENT TYPE
            st.markdown("## :violet[Top Payment Type]")
            
            # Reading Aggregated_Trans.csv
            aggregated_trans_df = pd.read_csv('Aggregated_Trans.csv')
            
            # Filtering data based on selected Year and Quarter
            filtered_trans_df = aggregated_trans_df[(aggregated_trans_df['Year'] == int(Year)) & (aggregated_trans_df['Quarter'] == int(Quarter))]
            
            # Group by 'Transaction_type' and aggregate
            grouped_trans_df = filtered_trans_df.groupby('Transaction_type').agg({
                'Transaction_count': 'sum',
                'Transaction_amount': 'sum'
            }).reset_index()

            # Sorting the DataFrame by 'Total_Transactions_amount' column in descending order
            sorted_trans_df = grouped_trans_df.sort_values(by='Transaction_amount', ascending=False)

            # Creating a bar chart using Plotly Express
            fig = px.bar(sorted_trans_df,
                        title='Transaction Types vs Total_Transactions',
                        x="Transaction_type",
                        y="Transaction_count",
                        orientation='v',
                        color='Transaction_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)

            st.plotly_chart(fig, use_container_width=False)

        # BAR CHART TRANSACTIONS - DISTRICT WISE DATA
        with col2:
        # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
            st.markdown("## :violet[Select any State to explore more]")
            selected_state = st.selectbox("",
                                ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'), index=30)
            
            # Reading Map_Trans.csv
            map_trans_df = pd.read_csv('Map_Trans.csv')
            
            # Filtering data based on selected Year, Quarter, and State
            filtered_map_trans_df = map_trans_df[(map_trans_df['Year'] == int(Year)) & (map_trans_df['Quarter'] == int(Quarter)) & (map_trans_df['State'] == selected_state)]
            
            # Group by 'District' and aggregate
            grouped_map_trans_df = filtered_map_trans_df.groupby('District').agg({
                'Count': 'sum',
                'Amount': 'sum'
            }).reset_index()

            # Creating a bar chart using Plotly Express
            fig = px.bar(grouped_map_trans_df,
                        title=selected_state,
                        x="District",
                        y="Count",
                        orientation='v',
                        color='Amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)

            st.plotly_chart(fig, use_container_width=True)

    #  ------------    -------------------------------
    if Type == "Users":
        df_user = pd.read_csv('Map_user_data.csv')
        df_state_names = pd.read_csv('state_names.csv')

            # Overall State Data - User App Opening Frequency
        st.markdown("## :violet[Overall State Data - User App Opening Frequency]")

            # Group by 'State' and aggregate
        grouped_user_df = df_user.groupby('State').agg({
                'RegisteredUser': 'sum',
                'AppOpens': 'sum'
            }).reset_index()

            # Merge with state_names_df to get the state names
        grouped_user_df['state'] = df_state_names['state']

            # Create choropleth map using Plotly Express
        fig_user = px.choropleth(
                grouped_user_df,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state',
                color='AppOpens',
                color_continuous_scale='sunset'
            )

        fig_user.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_user, use_container_width=True)

            # BAR CHART TOTAL USERS - DISTRICT WISE DATA
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox(
                '',
                ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat', 'haryana',
                'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
                'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal')
            )

            # Filter data based on selected State
        selected_user_df = df_user[(df_user['Year'] == int(Year)) & (df_user['Quarter'] == int(Quarter)) & (df_user['State'] == selected_state)]

            # Group by 'District' and aggregate
        grouped_user_district_df = selected_user_df.groupby('District').agg({
                'RegisteredUser': 'sum',
                'AppOpens': 'sum'
            }).reset_index()

            # Create a bar chart using Plotly Express
        fig_user_district = px.bar(
                grouped_user_district_df,
                title=selected_state,
                x='District',
                y='RegisteredUser',
                orientation='v',
                color='RegisteredUser',
                color_continuous_scale=px.colors.sequential.Agsunset
            )

        st.plotly_chart(fig_user_district, use_container_width=True)
    
if selected == "My-Profile":
    col1,col2 = st.columns([3,3],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.subheader(":white[Phone Pulse: ]",divider='rainbow')
        st.markdown("""
                    <div style="text-align: justify; font-size: 30px;">
                        <h3 style="color: purple;">The objective of this project is to:</h3>
                        <p style="font-size: 25px; text-align: justify;">
                            Retrieve data from the Phonepe Pulse GitHub repository, perform data transformation and cleansing,
                            insert it into a MySQL database, and develop a live geo-visualization dashboard using Streamlit and Plotly in Python.
                            The dashboard will present the data interactively and aesthetically, featuring a minimum of 10 diverse dropdown options
                            for users to select various facts and figures. The solution aims to be secure, efficient, and user-friendly, offering valuable
                            insights and information about the data within the Phonepe Pulse GitHub repository.
                        </p></div>""", unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("### :gray[Name:  ] :blue[Dinesh Dhamodharan]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:gray[Email:  ] dineshdin9600@gmail.com")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[My Project GitHub link] ⬇️")
        github_url = "https://github.com/DineshDhamodharan24/Phonepe-Pulse-Data-Visualization-and-Exploration"
        button_color = "#781734"
        # Create a button with a hyperlink
        button_html = f'<a href="{github_url}" target="_blank"><button style="font-size: 16px; background-color: {button_color}; color: #fff; padding: 8px 16px; border: none; border-radius: 4px;">GitHub My Phonepe Project</button></a>'
        st.markdown(button_html, unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[My Linkdin] ⬇️")
        Linkdin_url= "https://www.linkedin.com/in/dinesh-dhamodharan-2bbb9722b/"
        button_color = "#781734"
        button_html = f'<a href="{Linkdin_url}" target="_blank"><button style="font-size: 16px; background-color: {button_color}; color: #fff; padding: 8px 16px; border: none; border-radius: 4px;">My Linkdin profile</button></a>'
        st.markdown(button_html, unsafe_allow_html=True)