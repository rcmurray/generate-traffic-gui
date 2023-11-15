import matplotlib.pyplot as plt
import numpy as np

"""
Plot graphs with more readable xlims and ylims.
Parameters:
    time_x(list(ints)): The x values for the graph.
    gaussian_y(list(floats)): The y values for the graph.
"""
def lim_plots(time_x, gaussian_y):
    fig, ax = plt.subplots(figsize=(12, 6))
    x = time_x
    y = gaussian_y
    ax.plot(y)
    #the x axis should show 0 through time
    plt.xlim([0, len(time_x)-1])
    #the y axis shows twice the highest y value
    plt.ylim([0, max(gaussian_y) * 2])
    plt.xlabel("Time")
    plt.ylabel("Requests")
    plt.show()
    
"""
Parameters:
    mean(int): The mean of the distribution.
    sd(int): The standard deviation of the distribution.
    time(int): The number of points to generate.
    new_dist(list(lists)): The new distribution to follow. Should be in this form.
    [[end1,freq1], [end2,freq2]...] The first entry in the list should be the percentage of the graph this section of the distribution will go up to, and the second should be the probability that any random point generated with this distribution falls within that sections of the graph. For example, a distribution of [[0.5, 0.9], [1, 0.1]] will have 90% of points fall within the first half of the graph and 10% of points fall within the second half.  
Returns: 
    requests_y(list(floats)): a series of randomly generated numbers along said distribution.
"""
def unique_norm(middle, sd, time, custom_dist):
    #based off of the usual range of standard deviations: approximate, however.
    start = middle - sd * 4
    end = middle + sd * 4
    requests_y = []
    #for each point
    for i in range(time):
        rand_num = np.random.random()
        #the total number that rand_num must be below in order to fall into a certain probability block
        freq_sum = 0
        #for each of the distribution's blocks of probability
        for freq in range(len(custom_dist)):
            #ensures upper bound of probability is always increased
            #that way all points will eventually be added (because sum of all 
            freq_sum += custom_dist[freq][1]
            #if the random number is less than that sum
            if rand_num < freq_sum:
                #determine the range of the point's actual value
                upper_bound = start + ((abs(end)-start)*custom_dist[freq][0])
                #if this is the first probability block
                if freq == 0:
                    #then the range will be from 0 to the upper_bound
                    requests_y.append(np.random.uniform(start, upper_bound))
                    #exit this loop so it is not added again
                    break
                else:
                    requests_y.append(np.random.uniform(custom_dist[freq-1][0], upper_bound))
                    break
        #if we've reached the number of points requested
        if len(requests_y) == time:
            #leave loop
            break
    return requests_y