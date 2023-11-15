Welcome to the Generating Simulated Network Traffic program. Below is an overview of the program, a list of contents, explanations about how to add new simulated data specifications to graph_data.csv, and a list of possible future refinements. 

OVERVIEW:
This program is meant to be imbedded in a SAIL() Cloud Administration course. It generates graphs that resemble common load patterns as details in Module 5 of this course: random, continuous growth, spikes, and cycles. The main file, generate_interactive_graphs, is a Jupyter Notebook that contains interactive elements such as drop-down menus and sliders so users can change the output without interacting with a coding cell. Coding cells should be invisible to users, and no other file should be accessible to them either. 

CONTENTS:
-aux.py:
    Contains a graphing helper function and a helper function for creating custom distributions (i.e, not normal gaussian distribution.) Imported by continuous_growth.py, generate_cycles.py, generate_interative_graphs.ipynb, generate_gaussian.py,and generate_spikes.py.
    
-continuous_growth.py:
    Generates network traffic showing continuous growth. Imported by generate_interactive_graphs.ipynb.
    
-dev_tests:
    Contains Jupyter Notebook versions of continuous_growth.py, generate_cycles.py, generate_gaussian.py,and generate_spikes.py. These are intended for testing network traffic generation or new features, and are not accessed by the main program. 
    
-generate_cycles.py
    Generates cyclical network traffic.
    
-generate_gaussian.py:
    Generate random pattern network traffic. Has an additional function to combine multiple distributions into one. 
    
-generate_interactive_graphs.ipynb:
    As mentioned above, the main file where graphs described in graph_data.csv are generated when their respective question id is input. For interactivity, current contains the ability to change the id (to view other questions' corresponding graphs) and change the timeframe over which network traffic is being viewed (three options: daily, monthly, yearly). 
    
-generate_spikes.py:
    Generates network traffic with irregular spikes.
    
-graphs_data.csv
    'type' refers to one of the four load patterns detailed in Module 5. Valid entries are 'random', 'continuous', 'cycles', and 'spikes'. This determines which function is called in generate_interactive_graphs.
    'mean' refers to the general mean in all patterns, or the low mean for cycle generation. 
    'sd' refers to the general sd in all patterns, or the low sd for cycle generation.
    'time' is how many point should be generated for the graph. Consider have 24 (or a multiple of 24) for daily graphs, 30 (or a multiple of 24) for monthly graphs, and 365 (or a mutiple of it) for yearly graphs for ease of readability.
    'type_var1' refers to...
        random: ALWAYS None
        continuous: 'start', or the first value of the graph.
        cycles: 'high_mean', or the highest mean of the cycle portions of the graph.
        spikes: 'spike_sd', or the standard deviation when creating spikes in the graph.
    'type_var2' refers to...
        random: ALWAYS None
        continuous: 'growth', or the final value for an exponent of 1 version of the graph.
        cycles: 'high_sd', or the standard deviation of the cycle portions of the graph.
        spikes: 'spikes_frequency', or the percentage of points that are spikes. Since spikes are formed by changing the standard deviation, remember that not all spikes will be particularly dramatic.
    'type_var3' refers too...
        random: ALWAYS None
        continuous: 'exp' or the exponent of the graph. Should be increasingly small the more points there are in the graph. 1.0003, for example, provides a notable effect for time = 365
        cycles: 'set_cycles'. None produces a single, random cycle. Specified cycles should be in the form of a list of three entry lists, where the first value is the start of the cycle, the second is the highest point in the cycle, and the third is the end of the cycle. All entries should be in a range of (0, time). 
        spikes: ALWAYS None
    'custom_dist': None to use a normal distribution when generating number. For details on creating a custom_dist, see that question in the FAQ. 
    'graph': True to produce a graph within the function, False to not. Should be False for graphs generated with generate_interactive_graphs.ipynb. 
    'id': The problem number. All graphs of different timeframes related to the same problem should have the same id.
    'timeframe': The timeframe over which this graph is occuring. Valid entries: 'daily', 'monthly', 'yearly'. Ideally, all problems should have one graph for each timeframe.
    
-README.txt:
    You are here. Describes the program and its contents.
    
FAQ:
-How do I add a new question's graphs?
    All specifications for graph generation is contained within graphs_data.csv. See specifications of that file for what should go in each column of a new graph. 
-How do I design a custom distribution?
    Custom distributions are formed with a list of two entry lists. The first entry in the list should be the percentage of the graph this section of the distribution will go up to, and the second should be the probability that any random point generated with this distribution falls within that sections of the graph. For example, a distribution of [[0.5, 0.9], [1, 0.1]] will have 90% of points fall within the first half of the graph and 10% of points fall within the second half. The histogram code at the end of dev_tests/generate_gaussian.ipynb can help to visualize your new distribution for you. 
    
ACKNOWLEDGEMENTS:
Thank you to Leah Teffera, Chris Bogart, Chas Murray, Carolyn Rosé, Bruce McLaren, Majd Sakr, and Hayden Stec for their assistance, advice, and expertise that made this simulation possible. 

AUTHOR(S): 
Lex Miller (July-August 2023) 
[Your name (date worked on)]