# Matplotlib library for creating static, animated, and interactive visualizations in Python.
#import "matplotlib.pyplot"

#WEBSITE : https://matplotlib.org/stable/index.html#learn

#Types of Plot :
    # Line Chart
    # Scatter Chart
    # Bubble Chart
    # Bar Chart
    # Histogram
    # Pie Chart
    # Heatmap
    
#line Chart : (.plot(x,y))
    # - To display trend or changes over the time.
    # - Scenario : Trading Stocks price over time 
    # - X-axis: Time (any ordered series). Y-axis: Stock Price (A continuous variable showing
    #     progression or change over the X-axis).

#Scatter Chart : (.scatter(x,y) )
    # To explore potential correlations between two continuous variables.
    # Use Case: UberEats analyzing the relationship between ads cost and the revenue generated.
    # X-axis: Advertising Cost on ad
    # Y-axis: Sales / Revenue generated
    #.scatter()--> It only draws the bubble in the chart
    
# Bubble Chart : (.scatter(), .text() )
    # find “attractive” clusters considering multiple factors.
    # Use Case: To find an affordable city for a tech job.
    # X-axis: Growth% in Tech jobs
    # Y-axis: Avg Tech Salary
    # Bubble size: # of job openings / Cost of living
    #.scatter()--> It only draws the bubble in the chart and .text() --> writes the name on each bubble

# Histogram :( .hist() )
#     To understand the distribution of a dataset.
#     Use Case: Understand the distribution of users watch time on Youtube / 
#     X-axis: Watch time on Youtube(continuous variable)
#     Y-axis: Frequency(# of users)

# Bar Chart : ( .bar(x,y) ) #x = category name, y = value to display
#     To compare quantities across categories.
#     Use Case: Understand Amazon net sales by segment / total battery consumed by apps / Running total kms per day
#     X-axis: segments
#     Y-axis: Net sales amount($)
 
# Pie Chart : (.pie())
#     To show parts of a whole in percentage
#     Use Case: Understand the US Search Market Share (Google, Tesla, MS, Youtube, Apple, X, SpaceX etc..)
#               Understand the market cap split(large, medium, small) 
#               Equity sector allocation(Healthcare, Materials, Technology, Financial,Energy&Utility)

# Heatmap :
    # Understand how performance changes over the hours of the day and the days of the week.
    # Use Case: Analyzing peak usage times on Instagram throughout the week.
    # Two dimensions: hours of the day vs. days of the week.
    # Color bar: Indicating user activity levels.
    
    
#subplot() :

    #With the subplot() function you can draw multiple charts in one figure:

    # The subplot() function takes three arguments that describe the layout of the figure.
    # The layout is organized in rows and columns, which are represented by the first and second argument.
    # The third argument represents the index of the current plot.