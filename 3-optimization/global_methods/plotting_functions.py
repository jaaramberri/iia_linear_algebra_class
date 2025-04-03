import matplotlib.pyplot as plt

def pretty_plot_gs(xlim=None, ylim=None, xlabel=None, ylabel=None, title=None):
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    plt.legend()
    plt.show()
    return
    

def plot_single_run(result, algorithm_key='RW', num_iterations=200):
    """
    Plots the given optimization algorithm's progress over iterations in two subplots:
    - Left: sCurrent and sBest values
    - Right: costCurrent and costBest values

    Parameters:
        result (dict): Dictionary containing results of different optimization runs.
        algorithm_key (str): Key to access the algorithm results in the dictionary (e.g., 'RW', 'GD').
        num_iterations (int): Number of iterations to display on the x-axis. Default is 200.
    
    Returns:
        None
    """
    # Extract iteration count and the corresponding sCurrent and sBest values
    iterations = result[algorithm_key][0, :, 0]  # Iteration numbers
    s_current = result[algorithm_key][0, :, 1]   # sCurrent values
    s_best = result[algorithm_key][0, :, 2]      # sBest values
    cost_current = result[algorithm_key][0, :, 3]  # costCurrent values
    cost_best = result[algorithm_key][0, :, 4]     # costBest values

    # Create a figure with 1 row and 2 columns of subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

    # Left subplot: sCurrent and sBest values
    axs[0].plot(iterations, s_current, label='sCurrent')
    axs[0].plot(iterations, s_best, label='sBest')
    axs[0].set_xlim(0, num_iterations)
    axs[0].set_xlabel('Iteration')
    axs[0].set_ylabel('s Values')
    axs[0].set_title(f"{algorithm_key} Algorithm Single Run")
    axs[0].legend()

    # Right subplot: costCurrent and costBest values
    axs[1].plot(iterations, cost_current, label='costCurrent')
    axs[1].plot(iterations, cost_best, label='costBest')
    axs[1].set_xlim(0, num_iterations)
    axs[1].set_xlabel('Iteration')
    axs[1].set_ylabel('Cost Values')
    axs[1].set_title(f"{algorithm_key} Algorithm Single Run - Cost Function")
    axs[1].legend()

    # Adjust layout to prevent overlap of subplots
    plt.tight_layout()

    # Show the plot
    plt.show()

def pretty_plot_sa(xlim=None, ylim=None, xlabel=None, ylabel=None, title=None, colorbar=False):
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)
    if colorbar:
        plt.colorbar()
    plt.legend()
    plt.show()
    return