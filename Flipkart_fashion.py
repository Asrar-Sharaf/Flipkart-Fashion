
import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_excel('Flipkart Fashion Cleaned Data.xlsx', sheet_name='Sheet1')
    
# Descriptive Analysis
def describtive_Analysis(df):
    st.title("Descriptive Analysis")
    
    num = df.describe()
    cat = df.describe(include='O')

    # Numerical Descriptive Statistics
    st.subheader('Numerical Descriptive Statistics')
    st.dataframe(num.T.style.format(precision=2), height=430)
    
    # Add a separator or spacer
    st.markdown("---")  # Horizontal line for separation
    
    # Categorical Descriptive Statistics
    st.subheader('Categorical Descriptive Statistics')
    st.dataframe(cat.style.format(na_rep='N/A'), height=180)
    
# Univariate Analysis
def univariate_analysis(df):
    st.title("Univariate Analysis")

    #creating sidebars for filtering the dataset
    country = st.sidebar.selectbox('Select Country', ["All"] + df['Country of Origin'].unique().tolist())
    category = st.sidebar.selectbox('Select Product Category', ["All"] + df['category'].unique().tolist())
    sub_category = st.sidebar.selectbox('Select Sub_category', ["All"] + df['sub_category'].unique().tolist())
    Fabric_categories = st.sidebar.selectbox('Select Fabric_categories', ["All"] + df['Fabric_Categories'].unique().tolist())
    size = st.sidebar.selectbox('Select Size', ["All"] + df['Size'].unique().tolist())
    fit = st.sidebar.selectbox('Select Fit', ["All"] + df['Fit'].unique().tolist())
    customer_segment = st.sidebar.selectbox('Select Customer Segment', ["All"] + df['Ideal_For_Categories'].unique().tolist())
    show_data = st.sidebar.checkbox('Show Data', False)

    if show_data:
        st.header('Dataset Sample')
        st.dataframe(df.head(8))

    #this is to check if user choose something other than "All", the numbers in the visuals will change accordingly 
    if country != "All":
        df = df[df['Country of Origin'] == country]
    if category != "All":
        df = df[df['category'] == category]
    if sub_category != "All":
        df = df[df['sub_category'] == sub_category]
    if Fabric_categories != "All":
        df = df[df['Fabric_Categories'] == Fabric_categories]
    if size != "All":
        df = df[df['Size'] == size]
    if fit != "All":
        df = df[df['Fit'] == fit]
    if customer_segment != "All":
        df = df[df['Ideal_For_Categories'] == customer_segment]

    # Distribution of Product Sub-categories
    sub_category_fig= px.histogram(df, x="sub_category", title="Distribution of Product Sub-categories", color_discrete_sequence= ['#2E8B57'],nbins=30,width=700, height=500, marginal='violin')
    sub_category_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(sub_category_fig, use_container_width=True)

    
    # Fit Distribution
    fit_fig= px.histogram(df, x="Fit", title="Fit Distribution", color_discrete_sequence= ['#2E8B57'],nbins=30,width=700, height=500, marginal='violin')
    fit_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(fit_fig, use_container_width=True)

    
    # Product Sizes Distribution
    size_fig= px.histogram(df, x="Size", title="Distribution of Product Sizes", color_discrete_sequence= ['#2E8B57'],nbins=30,width=700, height=500, marginal='violin')
    size_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(size_fig, use_container_width=True)

    # Distribution of Product Fabric Categories
    Fabric_categories_fig = px.histogram(df, x="Fabric_Categories", title="Distribution of Product Fabric Categories", color_discrete_sequence=["#2E8B57"], width=750, height=500, marginal='rug',labels={"Fabric_Categories": "Fabric Categories"})
    Fabric_categories_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0', title="Fabric Categories"),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0', title="Count"))    
    st.plotly_chart(Fabric_categories_fig, use_container_width=True)

    # Frequency of Countries of Origin
    Country_fig = px.histogram(df,x='Country of Origin',title='Frequency of Countries of Origin',color_discrete_sequence=['#2E8B57'],marginal='violin')
    Country_fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    title_font=dict(size=20, color='#2E8B57'),
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0', title="Country of Origin"),
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0', title="Count"))
    st.plotly_chart(Country_fig, use_container_width=True)

    # Distribution of Customer Segments
    fig_ideal_fig = px.histogram(df,x="Ideal_For_Categories",title="Distribution of Customer Segments",color_discrete_sequence=["#2E8B57"],marginal="violin",)
    fig_ideal_fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_font=dict(size=20, color="#2E8B57"),
    xaxis=dict(showgrid=True, gridcolor="#d0f0c0", title="Customer Segment"),
    yaxis=dict(showgrid=True, gridcolor="#d0f0c0", title="Count"))    
    st.plotly_chart(fig_ideal_fig, use_container_width=True)

    # Distribution Products Categories
    category_fig = px.pie(df,names="category",title="Distribution Products Categories",color_discrete_sequence= ['#2E8B57', 'orange','yellow'],width=350,height=400)
    category_fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_font=dict(size=20, color="#2E8B57"))    
    st.plotly_chart(category_fig, use_container_width=True)


# Bivariate Analysis
def bivariate_analysis(df):
    st.title("Bivariate Analysis")

    #creating sidebars for filtering the dataset
    country = st.sidebar.selectbox('Select Country', ["All"] + df['Country of Origin'].unique().tolist())
    category = st.sidebar.selectbox('Select Product Category', ["All"] + df['category'].unique().tolist())
    sub_category = st.sidebar.selectbox('Select Sub_category', ["All"] + df['sub_category'].unique().tolist())
    Fabric_categories = st.sidebar.selectbox('Select Fabric_categories', ["All"] + df['Fabric_Categories'].unique().tolist())
    size = st.sidebar.selectbox('Select Size', ["All"] + df['Size'].unique().tolist())
    fit = st.sidebar.selectbox('Select Fit', ["All"] + df['Fit'].unique().tolist())
    customer_segment = st.sidebar.selectbox('Select Customer Segment', ["All"] + df['Ideal_For_Categories'].unique().tolist())
    show_data = st.sidebar.checkbox('Show Data', False)

    if show_data:
        st.header('Dataset Sample')
        st.dataframe(df.sample(5))


    if country != "All":
        df = df[df['Country of Origin'] == country]
    if category != "All":
        df = df[df['category'] == category]
    if sub_category != "All":
        df = df[df['sub_category'] == sub_category]
    if Fabric_categories != "All":
        df = df[df['Fabric_Categories'] == Fabric_categories]
    if size != "All":
        df = df[df['Size'] == size]
    if fit != "All":
        df = df[df['Fit'] == fit]
    if customer_segment != "All":
        df = df[df['Ideal_For_Categories'] == customer_segment]

    
    # Top 10 Sales by Subcategory
    total_sales_by_subcategory = df.groupby('sub_category')[['selling_price']].sum().sort_values(by='selling_price', ascending=False).reset_index().head(10)
    total_sales_by_subcategory_fig = px.histogram(total_sales_by_subcategory,x='sub_category',y='selling_price',title='Top 10 Sales by Subcategory',color_discrete_sequence=["#2E8B57"], marginal='box',width=750,height=500)
    total_sales_by_subcategory_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(total_sales_by_subcategory_fig, use_container_width=True)

    
    # Average Discount by Subcategory
    avg_discount_by_subcategory = df.groupby('sub_category')['discount_percentage'].mean().reset_index().head(10)
    avg_discount_by_subcategory_fig = px.line(avg_discount_by_subcategory, x='sub_category',y='discount_percentage',title='Average Discount by Subcategory', color_discrete_sequence=["#2E8B57"], width=750, height=500, markers=True)
    avg_discount_by_subcategory_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white', 
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(avg_discount_by_subcategory_fig, use_container_width=True)

    
    # Top 10 Rated Products by Subcategory
    avg_rating_by_sub_category = df.groupby('sub_category')[['average_rating']].mean().sort_values(by='average_rating', ascending=False).reset_index().head(10)
    avg_rating_by_sub_category_fig = px.bar(avg_rating_by_sub_category,x='sub_category',y='average_rating',color='sub_category', title='Top 10 Rated Products by Subcategory',text='average_rating', width=750,height=500, color_discrete_sequence=px.colors.sequential.Greens)
    avg_rating_by_sub_category_fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_font=dict(size=20, color="#2E8B57"),
    xaxis=dict(showgrid=True, gridcolor="#d0f0c0", title="Ideal For Categories"),
    yaxis=dict(showgrid=True, gridcolor="#d0f0c0", title="Count"))
    st.plotly_chart(avg_rating_by_sub_category_fig, use_container_width=True)


    # Total Sales by Category'
    total_sales_by_category = df.groupby('category')[['selling_price']].sum().sort_values(by='selling_price',ascending=False).reset_index()
    total_sales_by_category_fig = px.bar(total_sales_by_category, x='category', y='selling_price', title='Total Sales by Category', color_discrete_sequence=['#2E8B57'],width=600, height=400)
    total_sales_by_category_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(total_sales_by_category_fig, use_container_width=True)

    
    # Top 10 Brands by Total Sales
    total_sales_by_brand = df.groupby('brand_name')[['selling_price']].sum().sort_values(by='selling_price',ascending=False).head(10)
    total_sales_by_brand_fig = px.bar(total_sales_by_brand.reset_index(),x='brand_name',y='selling_price',color='brand_name',  title='Top 10 Brands by Total Sales',text='selling_price',color_discrete_sequence=px.colors.sequential.Greens, width=600, height=400)
    total_sales_by_brand_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(total_sales_by_brand_fig, use_container_width=True)

    # Top 10 Average Discount by Brands
    avg_discount_by_brand = df.groupby('brand_name')[['discount_percentage']].mean().sort_values(by='discount_percentage',ascending=False).reset_index().head(10)
    avg_discount_by_brand_fig = px.bar(avg_discount_by_brand,x='brand_name',y='discount_percentage',color='brand_name', title='Top 10 Average Discount by Brands',text='discount_percentage', color_discrete_sequence=px.colors.sequential.Greens, width=750,height=500)
    avg_discount_by_brand_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(avg_discount_by_brand_fig, use_container_width=True)


    # Top Total Sales by Fabric
    total_sales_by_fabric = df.groupby('Fabric')[['selling_price']].sum().sort_values(by='selling_price', ascending=False).reset_index().head(10)
    total_sales_by_fabric_fig = px.histogram(total_sales_by_fabric,x='Fabric',y='selling_price',title='Top Total Sales by Fabric',color_discrete_sequence=["#2E8B57"],width=750,height=500,marginal='box',)
    total_sales_by_fabric_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))  
    st.plotly_chart(total_sales_by_fabric_fig, use_container_width=True)

    
    # Distribution of Top Average Selling Price by Fabric Type
    avg_price_by_fabric = df.groupby('Fabric')['selling_price'].mean().sort_values(ascending=False).reset_index().head(10)
    avg_price_by_fabric_fig = px.histogram(avg_price_by_fabric,x='Fabric',y='selling_price',title='Distribution of Top Average Selling Price by Fabric Type',color='Fabric',color_discrete_sequence=px.colors.sequential.Greens,width=750,height=500, marginal='rug',)
    avg_price_by_fabric_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(avg_price_by_fabric_fig, use_container_width=True)

    
    # Total Sales by Fabric Category
    total_sales_by_fabric_category = df.groupby('Fabric_Categories')['selling_price'].sum().reset_index()
    total_sales_by_fabric_category_fig = px.histogram(total_sales_by_fabric_category, x="Fabric_Categories", y="selling_price",title="Total Sales by Fabric Category", color_discrete_sequence=["#2E8B57"], width=750, height=500, marginal='violin')
    total_sales_by_fabric_category_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0')) 
    st.plotly_chart(total_sales_by_fabric_category_fig, use_container_width=True)

    
    # Top Selling Price by Pattern
    selling_price_by_pattern = df.groupby('Pattern')[['selling_price']].sum().sort_values(by='selling_price',ascending=False).reset_index().head(10)
    selling_price_by_pattern_fig = px.line(selling_price_by_pattern,x='Pattern',y='selling_price',markers=True, title='Top Selling Price by Pattern',color_discrete_sequence=["#2E8B57"],width=750,height=500)
    selling_price_by_pattern_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(selling_price_by_pattern_fig, use_container_width=True)


    # Top Total Sales by Sellers
    top_sellers = df.groupby('seller')[['selling_price']].sum().sort_values(by='selling_price',ascending=False).reset_index().head(10)
    top_seller_fig = px.histogram(top_sellers, x="seller", y="selling_price", title="Top Total Sales by Sellers", color_discrete_sequence=["#2E8B57"], marginal='box', width=700, height=600)
    top_seller_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(top_seller_fig, use_container_width=True)

    
    # Average Rating by Country of Origin
    avg_rating_by_country_of_origin = df.groupby(['Country of Origin'])[['average_rating']].mean().sort_values(by='average_rating', ascending=False).reset_index()
    avg_rating_by_country_of_origin_fig= px.histogram(avg_rating_by_country_of_origin, x='Country of Origin', y='average_rating', title='Average Rating by Country of Origin', color_discrete_sequence=["#2E8B57"], width=750, height=500)
    avg_rating_by_country_of_origin_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(avg_rating_by_country_of_origin_fig, use_container_width=True)

    
    # Top Total Sales by Top Sizen
    total_sales_by_size = df.groupby('Size')[['selling_price']].sum().sort_values(by='selling_price', ascending=False).reset_index().head(5)
    total_sales_by_size_fig = px.pie(total_sales_by_size, values='selling_price', names='Size', title='Top Total Sales by Top Size', color_discrete_sequence=px.colors.sequential.Greens, width=500, height=400)
    total_sales_by_size_fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(total_sales_by_size_fig, use_container_width=True)

    
    # Top 10 Average Discount by Brands
    total_sales_by_ideal_for = df.groupby('Ideal_For_Categories')[['selling_price']].sum().sort_values(by='selling_price', ascending=False).reset_index()
    total_sales_by_ideal_for_fig = px.histogram(total_sales_by_ideal_for, x='Ideal_For_Categories', y='selling_price', title='Total Sales by Customer Segment', color_discrete_sequence=["#2E8B57"], width=700,height=500, marginal='violin')
    total_sales_by_ideal_for_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(total_sales_by_ideal_for_fig, use_container_width=True)


    # Total Sales by Stock
    availability_sales = df.groupby('is_out_of_stock')['selling_price'].sum().sort_values(ascending=False).reset_index()
    availability_sales_fig= px.pie(df, names="is_out_of_stock",  values="selling_price", title="Total Sales by Stock",color_discrete_sequence= ['#2E8B57', '#FFB84D'],width=350,height=400)
    availability_sales_fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_font=dict(size=20, color="#2E8B57"))    
    st.plotly_chart(availability_sales_fig, use_container_width=True)


    # Top Five Selling Products by Brand and Sub-category
    top_selling_products_by_brand = df.groupby(['sub_category', 'brand_name'])[['selling_price']].sum().sort_values(by='selling_price', ascending=False).reset_index().head(5)
    top_selling_products_by_brands_fig = px.bar(top_selling_products_by_brand,x='brand_name',y='selling_price',color='sub_category',title='Top Five Selling Products by Brand and Sub-category',color_discrete_sequence= ['#14523D', '#2E8B57', '#90CDA0'], width=600,height=500,)
    top_selling_products_by_brands_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(top_selling_products_by_brands_fig, use_container_width=True)


    # Top Five Average Discount Percentage for Sub-Categories and Brands
    ave_discount_by_subcategory_brand = df.groupby(['sub_category', 'brand_name'])[['discount_percentage']].mean().sort_values(by='discount_percentage', ascending=False).reset_index().head(5)
    ave_discount_by_subcategory_brand_fig = px.bar(ave_discount_by_subcategory_brand,x='brand_name',y='discount_percentage',color='sub_category',color_discrete_sequence= ['#2E8B57', '#8bd38d', '#388e3c', '#006400', '#d9f7be'], width=600,height=500,labels={'discount_percentage': 'Average Discount Percentage'},title="Top Five Average Discount Percentage for Sub-Categories and Brands")
    ave_discount_by_subcategory_brand_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(ave_discount_by_subcategory_brand_fig, use_container_width=True)


    # Total Sales by Sellers and Sub-category
    sales_by_subcategory_seller = df.groupby(['sub_category', 'seller'])[['selling_price']].sum().sort_values(by='selling_price', ascending=False).reset_index().head(10)
    sales_by_subcategory_seller_fig = px.bar(sales_by_subcategory_seller, x='seller',y='selling_price',color='sub_category',title='Total Sales by Sellers and Sub-category',color_discrete_sequence= ['#14523D', '#2E8B57', '#90CDA0'], width=750, height=500)
    sales_by_subcategory_seller_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(sales_by_subcategory_seller_fig, use_container_width=True)


    # Top Three Sales by Fabric, and Sub-category
    sales_fabric_subcategory = df.groupby(['Fabric', 'sub_category'])[['selling_price']].sum().sort_values(by='selling_price', ascending=False).head(3).reset_index()
    sales_fabric_subcategory_fig = px.bar(sales_fabric_subcategory, x='sub_category',y='selling_price',color='Fabric',title='Top Three Sales by Fabric, and Sub-category',color_discrete_sequence= ['#2E8B57', '#90CDA0'], width=450,height=500)
    sales_fabric_subcategory_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0')) 
    st.plotly_chart(sales_fabric_subcategory_fig, use_container_width=True)


    # Average Discount by Subcategory, and Country of Origin
    avg_discount_by_subcategory_country = df.groupby(['sub_category', 'Country of Origin'])[['discount_percentage']].mean().sort_values(by='discount_percentage', ascending=False).reset_index().head(10)
    avg_discount_by_subcategory_country_fig = px.bar(avg_discount_by_subcategory_country, x='sub_category', y='discount_percentage', color='Country of Origin', title='Average Discount by Subcategory, and Country of Origin', color_discrete_sequence= ['#2E8B57', '#8bd38d', '#388e3c', '#006400', '#d9f7be'], width=700, height=500,)
    avg_discount_by_subcategory_country_fig.update_layout(
    plot_bgcolor='white',  
    paper_bgcolor='white', 
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'), 
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(avg_discount_by_subcategory_country_fig, use_container_width=True)

    # Top 5 Countries Sales by Category
    top_countries_sales_by_category = df.groupby(['Country of Origin', 'category'])[['selling_price']].sum().sort_values(by='selling_price', ascending=False).head(5).reset_index()
    top_countries_sales_by_category_fig = px.bar(top_countries_sales_by_category, x='Country of Origin',y='selling_price',color='category',title='Top 5 Countries Sales by Category',color_discrete_sequence=["#2E8B57", '#90CDA0'],width=700,height=500)
    top_countries_sales_by_category_fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white', 
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(top_countries_sales_by_category_fig, use_container_width=True)


    # Average of Top 5 Brands and Fabric by Average Rating and Discount Percentage
    brand_rating_discount_fabric_brand = df.groupby(['brand_name', 'Fabric'])[['average_rating', 'discount_percentage']].mean().sort_values(by='average_rating', ascending=False).reset_index().head(5)
    brand_rating_discount_fabric_brand_fig = px.bar(brand_rating_discount_fabric_brand, x='brand_name',y=['average_rating', 'discount_percentage'],color='Fabric',color_discrete_sequence= ['#14523D', '#2E8B57', '#90CDA0', '#d9f7be'], width=550, height=500,title="Average of Top 5 Brands and Fabric by Average Rating and Discount Percentage")
    brand_rating_discount_fabric_brand_fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',  
    title_font=dict(size=20, color='#2E8B57'), 
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(brand_rating_discount_fabric_brand_fig, use_container_width=True)

    # Top Average Selling Price by Sub-Category, Fabric, and Size
    total_sale_by_category_fabric_size = df.groupby(['sub_category', 'Fabric', 'Size'])[['selling_price']].mean().sort_values(by='selling_price', ascending=False).reset_index().head(5)
    total_sale_by_category_fabric_size_fig = px.bar(total_sale_by_category_fabric_size, x='Fabric', y='selling_price', color='sub_category', facet_col='Size',color_discrete_sequence= ['#A8E6A3 ', '#388E3C', '#006400', '#66BB6A', '#1B5E20'], width=750, height=500, labels={'selling_price': 'Average Selling Price'}, title="Top Average Selling Price by Sub-Category, Fabric, and Size")
    total_sale_by_category_fabric_size_fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white',
    title_font=dict(size=20, color='#2E8B57'),  
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),  
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))
    st.plotly_chart(total_sale_by_category_fabric_size_fig, use_container_width=True)


    # Top 5 Average Discounts by Category, Subcategory, and Fabric
    avg_discount_by_category_fabric_subcategory = df.groupby(['category', 'sub_category', 'Fabric'])[['discount_percentage']].mean().sort_values(by='discount_percentage', ascending=False).reset_index().head(5)
    avg_discount_by_category_fabric_subcategory_fig = px.bar(avg_discount_by_category_fabric_subcategory, x='sub_category', y='discount_percentage', color='Fabric', title='Top 5 Average Discounts by Category, Subcategory, and Fabric',facet_col='category',color_discrete_sequence=px.colors.sequential.Greens, width=750, height=500, labels={"discount_percentage": "Average Discount (%)","sub_category": "Subcategory","Fabric": "Fabric Type","category": "Category"})
    avg_discount_by_category_fabric_subcategory_fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    title_font=dict(size=20, color='#2E8B57'),
    xaxis=dict(showgrid=True, gridcolor='#d0f0c0'),
    yaxis=dict(showgrid=True, gridcolor='#d0f0c0'))    
    st.plotly_chart(avg_discount_by_category_fabric_subcategory_fig, use_container_width=True)

st.sidebar.title("Flipkart Fashion Dashboard")
page = st.sidebar.radio("Choose an Analysis",("Describtive Analysis", "Univariate Analysis", "Bivariate Analysis"))

if page == "Describtive Analysis":
    describtive_Analysis(df)
elif page == "Univariate Analysis":
    univariate_analysis(df)
elif page == "Bivariate Analysis":
    bivariate_analysis(df)
